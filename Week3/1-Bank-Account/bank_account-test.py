import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rado", 0, "$")
        self.rado = BankAccount("Rado", 1000, "BGN")
        self.ivo = BankAccount("Ivo", 0, "BGN")
        self.history = []

    def test_init(self):
        self.assertTrue(isinstance(self.account, BankAccount))
        self.assertEqual(self.account.name, "Rado")
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.currency, "$")
        self.assertEqual(self.history, [])

    def test_str(self):
        needed_result = 'Bank account for Rado with balance of 0$'
        self.assertEqual(str(self.account), needed_result)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 500)
        with self.assertRaises(ValueError):
            self.account.deposit(-5)

    def test_get_balance(self):
        balance = self.account.get_balance()
        self.assertEqual(self.account.balance, balance)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)
        self.account.withdraw(1000)
        self.assertEqual(self.account.balance, 0)

    def test_transfer_to(self):
        result = self.rado.transfer_to(self.ivo, 500)
        self.assertTrue(result)
        with self.assertRaises(ValueError):
            self.account.transfer_to(self.ivo, 500)
        self.assertEqual(self.rado.balance, 500)
        self.assertEqual(self.ivo.balance, 500)

    def test_transfer_to_more_money_that_we_have(self):
        self.assertFalse(self.ivo.transfer_to(self.rado, 500))


if __name__ == '__main__':
    unittest.main()
