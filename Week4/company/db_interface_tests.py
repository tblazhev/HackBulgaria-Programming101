import unittest
from db_interface import DBInterface
from subprocess import call
import os


class DbIntTests(unittest.TestCase):
    def setUp(self):
        call("py create_company_test.py", shell=True)
        self.dbi = DBInterface("company_test.db")
        self.data = [{
            "id": 1,
            "name": "Ivan Ivanov",
            "monthly_salary": 5000,
            "yearly_bonus": 10000,
            "position": "Software Developer"
        }, {
            "id": 2,
            "name": "Rado Rado",
            "monthly_salary": 500,
            "yearly_bonus": 0,
            "position": "Technical Support Intern"
        }, {
            "id": 3,
            "name": "Ivo Ivo",
            "monthly_salary": 10000,
            "yearly_bonus": 100000,
            "position": "CEO"
        }, {
            "id": 4,
            "name": "Petar Petrov",
            "monthly_salary": 3000,
            "yearly_bonus": 1000,
            "position": "Marketing Manager"
        }, {
            "id": 5,
            "name": "Maria Georgieva",
            "monthly_salary": 8000,
            "yearly_bonus": 10000,
            "position": "COO"
        }]

    def test_get_employees(self):
        data = self.dbi.get_employees()
        self.assertEqual(self.data, data)

    def test_get_monthly_expenses(self):
        self.assertEqual(26500, self.dbi.get_monthly_expenses())

    def test_get_yearly_expenses(self):
        self.assertEqual(439000, self.dbi.get_yearly_expenses())

    def test_add_employee(self):
        new_entry = {
            "name": "Tedi",
            "monthly_salary": 20000,
            "yearly_bonus": 10000,
            "position": "Team Lead"
        }
        self.assertTrue(self.dbi.add_employee(new_entry))
        new_entry["id"] = 6
        self.data.append(new_entry)
        self.assertEqual(self.data, self.dbi.get_employees())

    def test_delete_employee_by_id(self):
        self.assertTrue(self.dbi.delete_employee_by_id(5))
        self.data.pop()
        self.assertEqual(self.data, self.dbi.get_employees())

    def test_update_employee_by_id(self):
        updated_info = {
            "id": 2,
            "name": "Rado Rado",
            "monthly_salary": 2000,
            "yearly_bonus": 2000,
            "position": "Senior Technical Support"
        }
        self.assertTrue(self.dbi.update_employee_by_id(2, updated_info))
        self.data[1] = updated_info
        self.assertEqual(self.data, self.dbi.get_employees())

    def tearDown(self):
        script_path = os.path.dirname(os.path.realpath(__file__))
        try:
            os.remove(script_path + "/company_test.db")
        except:
            pass

if __name__ == '__main__':
    unittest.main()
