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
        self.dict_cursor = self.conn.cursor()
        self.dict_cursor.row_factory = dict_factory

    def get_employees(self):
        query = "SELECT * FROM employees"
        result = self.dict_cursor.execute(query).fetchall()
        return result

    def get_monthly_expenses(self):
        query = "SELECT SUM(monthly_salary) AS total FROM employees"
        result = self.dict_cursor.execute(query).fetchone()
        return result["total"]

    def get_yearly_expenses(self):
        total_expenses = 0
        total_expenses += self.get_monthly_expenses() * 12
        query = "SELECT SUM(yearly_bonus) AS bonuses FROM employees"
        result = self.dict_cursor.execute(query).fetchone()
        total_expenses += result["bonuses"]
        return total_expenses

    def add_employee(self, emp_dict):
        query = "INSERT INTO employees VALUES(NULL, ?, ?, ?, ?)"
        data_to_insert = (
            emp_dict["name"],
            emp_dict["monthly_salary"],
            emp_dict["yearly_bonus"],
            emp_dict["position"]
        )
        self.dict_cursor.execute(query, data_to_insert)
        self.conn.commit()
        return True

    def delete_employee_by_id(self, emp_id):
        query = "DELETE FROM employees WHERE id = ?"
        self.dict_cursor.execute(query, (emp_id,))
        self.conn.commit()
        return True

    def update_employee_by_id(self, emp_id, updated_info):
        query = "UPDATE employees SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?"
        data_tuple = (
            updated_info["name"],
            updated_info["monthly_salary"],
            updated_info["yearly_bonus"],
            updated_info["position"],
            emp_id
        )
        self.dict_cursor.execute(query, data_tuple)
        return True
