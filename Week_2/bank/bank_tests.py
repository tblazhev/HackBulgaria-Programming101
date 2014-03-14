import unittest
import bank


class BankTest(unittest.TestCase):
    """docstring for BankTest"""
    def setUp(self):
        bank.balance = 0

    def test_get_balance(self):
        self.assertEqual(0, bank.get_balance())

    def test_deposit_money(self):
        self.assertTrue(bank.deposit_money(100))
        self.assertEqual(100, bank.get_balance())

    def test_deposit_negative_money(self):
        self.assertTrue(False is bank.deposit_money(-100))

    def test_withdraw_money(self):
        bank.balance = 200
        self.assertTrue(bank.withdraw_money(100))
        self.assertEqual(100, bank.get_balance())

    def test_withdraw_negative_money(self):
        self.assertTrue(not bank.withdraw_money(-100))

    def test_withdraw_more_money_than_balance(self):
        bank.balance = 100
        self.assertTrue(not bank.withdraw_money(200))

if __name__ == '__main__':
    unittest.main()
