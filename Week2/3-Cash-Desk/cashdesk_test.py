import unittest
from cashdesk import Bill


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(10)
        self.bill_2 = Bill(11)
        self.bill_3 = Bill(10)

    def test_init(self):
        self.assertEqual(self.bill, 10)

    def test_int(self):
        self.assertEqual(int(self.bill), 10)

    def test_amount_in_bill(self):
        with self.assertRaises(AttributeError):
            self.bill.amount

    def test_str_dunder_for_bill(self):
        self.assertEqual(str(self.bill), "A 10$ bill.")

    def test_repr_dunder_for_bill(self):
        self.assertEqual(repr(self.bill), "A 10$ bill.")

    def test_eq_between_bills_when_not_same(self):
        self.assertTrue(self.bill != self.bill_2)

    def test_eq_between_bills_when_same(self):
        self.assertTrue(self.bill == self.bill_3)

    def test_can_hash_bill(self):
        self.assertIsNotNone(hash(self.bill))

    def test_can_put_bill_in_dictionary(self):
        money_holder = {}
        money_holder[self.bill] = 1
        self.assertTrue(self.bill in money_holder)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bill = Bill(-10)

    def test_value_error_raises_from_zero_amount(self):
        with self.assertRaises(ValueError):
            self.bill = Bill(0)

    def test_type_error_raises_from_float_amount(self):
        with self.assertRaises(TypeError):
            self.bill = Bill(0.5)


if __name__ == '__main__':
    unittest.main()
