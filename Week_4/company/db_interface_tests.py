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

    def tearDown(self):
        script_path = os.path.dirname(os.path.realpath(__file__))
        try:
            os.remove(script_path + "/company_test.db")
        except:
            pass

if __name__ == '__main__':
    unittest.main()
