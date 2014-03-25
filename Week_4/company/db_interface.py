import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DBInterface():
    """docstring for DBInterface"""
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = dict_factory

    def get_employees(self):
        query = "SELECT * FROM employees"
        result = self.cursor.execute(query).fetchall()
        return result

    def get_monthly_expenses(self):
        query = "SELECT SUM(monthly_salary) AS total FROM employees"
        result = self.cursor.execute(query).fetchone()
        return result["total"]

    def get_yearly_expenses(self):
        total_expenses = 0
        total_expenses += self.get_monthly_expenses() * 12
        query = "SELECT SUM(yearly_bonus) AS bonuses FROM employees"
        result = self.cursor.execute(query).fetchone()
        total_expenses += result["bonuses"]
        return total_expenses
