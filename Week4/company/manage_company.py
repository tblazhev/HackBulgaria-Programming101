import sqlite3


def list_employees(self, cursor):
    sql = "SELECT id, name, position FROM employees"
    result = cursor.execute(sql)
    for row in result:
        print(row)


def main():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    while True:
        pass

if __name__ == '__main__':
    main()
