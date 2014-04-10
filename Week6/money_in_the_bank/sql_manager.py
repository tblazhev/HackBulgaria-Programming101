import sqlite3
from Client import Client
import re
import string
import hashlib
import time
from smtplib import SMTP
import gmail_config
import random


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                time_of_last_failed_login INTEGER DEFAULT 0,
                number_of_failed_attempts INTEGER DEFAULT 0,
                pass_reset_code TEXT,
                pass_reset_code_timestamp INTEGER)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def register(username, email, password):
    insert_sql = "insert into clients (username, email, password) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, email, hash_string(password)))
    conn.commit()


def is_blocked_user(username, int_timestamp):
    query = "SELECT time_of_last_failed_login, number_of_failed_attempts FROM clients WHERE username = ?"
    row = cursor.execute(query, (username,)).fetchone()
    if row is None:
        return False
    if int_timestamp - row[0] < 300 and row[1] >= 5:
        return True
    return False


def get_user(username, password):
    select_query = "SELECT id, username, email, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, hash_string(password)))
    user = cursor.fetchone()
    return user


def login(username, password):
    int_timestamp = int(time.time())

    is_blocked = is_blocked_user(username, int_timestamp)
    if is_blocked:
        print("You have been blocked for 5 minutes. Please wait patiently.")
        return False

    user = get_user(username, password)

    if(user):
        query = "UPDATE clients SET number_of_failed_attempts = 0 WHERE username = ?"
        cursor.execute(query, (username,))
        conn.commit()
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        query = "UPDATE clients SET number_of_failed_attempts = number_of_failed_attempts + 1, time_of_last_failed_login = ? WHERE username = ?"
        cursor.execute(query, (int_timestamp, username))
        conn.commit()
        return False


def check_for_strong_password(password):
    if len(password) <= 8:
        return False

    if not re.search('\d+', password):
        return False
    if not (re.search('[a-z]', password) and re.search('[A-Z]', password)):
        return False

    special_characters = set(string.punctuation)
    has_special_chars = False
    for c in password:
        if c in special_characters:
            has_special_chars = True
            break
    if has_special_chars is False:
        return False

    return True


def hash_string(password):
    m = hashlib.sha1()
    m.update(password.encode("UTF-8"))
    return m.hexdigest()


def check_password(password, hashed_password):
    resulted_hash = hash_string(password)
    return resulted_hash == hashed_password


def generate_random_reset_code(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def insert_reset_code(user_id, code):
    int_timestamp = int(time.time())
    data = (code, int_timestamp, user_id)
    query = "UPDATE clients SET pass_reset_code = ?, pass_reset_code_timestamp = ? WHERE id = ?"
    cursor.execute(query, (data))
    conn.commit()


def send_change_password(logged_user):
    gmail_sender = gmail_config.get_email()
    gmail_passwd = gmail_config.get_password()
    random_reset_code = hash_string(generate_random_reset_code())

    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    TO = logged_user.get_email()
    SUBJECT = 'Password Reset'
    TEXT = 'You have requested to change your password. Here is your verification_code:\n' + random_reset_code
    BODY = '\r\n'.join([
        'To: %s' % TO,
        'From: %s' % "noreply@console.hackbulgaria.com",
        'Subject: %s' % SUBJECT,
        '', TEXT
    ])

    try:
        server.sendmail("noreply@console.hackbulgaria.com", [TO], BODY)
        insert_reset_code(logged_user.get_id(), random_reset_code)
        print ('An email with a verification code has been sent.')
    except:
        print ("Error sending mail.")
    server.quit()


def change_password(logged_user, new_pass):
    new_pass_hashed = hash_string(new_pass)
    update_sql = "UPDATE clients SET password = ?, pass_reset_code = '' WHERE id = ?"
    cursor.execute(update_sql, (new_pass_hashed, logged_user.get_id()))
    conn.commit()


def is_valid_verification_code(logged_user, code):
    if code == '':
        return False

    int_timestamp = int(time.time())
    query = "SELECT pass_reset_code, pass_reset_code_timestamp FROM clients WHERE id = ?"
    data = (logged_user.get_id(),)
    row = cursor.execute(query, data).fetchone()
    if row is None:
        return False
    if row[0] != code or int_timestamp - row[1] > 600:
        return False
    return True
