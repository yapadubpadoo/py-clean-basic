import unittest
from app.entities.saving_account import SavingAccount


class TestSavingAccount(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_account_name(self):
        s = SavingAccount(account_id=1, name='John',
                          lastname='Doe', balance=1000)
        self.assertEqual(s.get_account_name(), "John Doe")

    def test_cannot_withdraw_if_balance_is_not_enough(self):
        s = SavingAccount(account_id=1, name='John',
                          lastname='Doe', balance=1000)
        self.assertEqual(s.can_withdraw(1001), 'NO')

    def test_can_withdraw_if_balance_is_enough(self):
        s = SavingAccount(account_id=1, name='John',
                          lastname='Doe', balance=1000)
        self.assertEqual(s.can_withdraw(500), 'YES')
