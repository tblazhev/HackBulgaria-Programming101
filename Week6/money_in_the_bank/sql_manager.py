import sqlite3
from Client import Client
import re
import string
import hashlib
import time


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
                number_of_failed_attempts INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_pass_hashed = hash_password(new_pass)
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass_hashed, logged_user.get_id()))
    conn.commit()


def register(username, email, password):
    insert_sql = "insert into clients (username, email, password) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, email, hash_password(password)))
    conn.commit()


def is_blocked_user(username, int_timestamp):
    query = "SELECT time_of_last_failed_login, number_of_failed_attempts FROM clients WHERE username = ?"
    row = cursor.execute(query, (username,)).fetchone()
    if int_timestamp - row[0] < 300 and row[1] >= 5:
        return True
    return False


def get_user(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, hash_password(password)))
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
        return Client(user[0], user[1], user[2], user[3])
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


def hash_password(password):
    m = hashlib.sha1()
    m.update(password.encode("UTF-8"))
    return m.hexdigest()


def check_password(password, hashed_password):
    resulted_hash = hash_password(password)
    return resulted_hash == hashed_password
