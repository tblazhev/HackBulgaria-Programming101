import sqlite3


def create_tables(cursor):
    cursor.execute("""CREATE TABLE employees
                    (id INTEGER PRIMARY KEY, name text, monthly_salary int, yearly_bonus int, position text)""")


def insert(item, cursor):
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]
    data_to_insert = (name, monthly_salary, yearly_bonus, position)

    query = "INSERT INTO employees VALUES(NULL, ?, ?, ?, ?)"
    cursor.execute(query, data_to_insert)

data = [{
    # "id": 1,
    "name": "Ivan Ivanov",
    "monthly_salary": 5000,
    "yearly_bonus": 10000,
    "position": "Software Developer"
}, {
    # "id": 2,
    "name": "Rado Rado",
    "monthly_salary": 500,
    "yearly_bonus": 0,
    "position": "Technical Support Intern"
}, {
    # "id": 3,
    "name": "Ivo Ivo",
    "monthly_salary": 10000,
    "yearly_bonus": 100000,
    "position": "CEO"
}, {
    # "id": 4,
    "name": "Petar Petrov",
    "monthly_salary": 3000,
    "yearly_bonus": 1000,
    "position": "Marketing Manager"
}, {
    # "id": 5,
    "name": "Maria Georgieva",
    "monthly_salary": 8000,
    "yearly_bonus": 10000,
    "position": "COO"
}]

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

create_tables(cursor)

for item in data:
    insert(item, cursor)

conn.commit()
conn.close()
