import unittest
from unittest.mock import MagicMock
from app.use_cases.bank_account_use_cases import BankAccountUseCases


class TestBankAccountUseCases(unittest.TestCase):
    def setUp(self):
        BankAccountUseCases.__instance = None
        pass

    def test_update_saving_account_with_saving_interest(self):
        saving_account = MagicMock()
        saving_account.get_balance = MagicMock(return_value=1000)
        saving_account.set_balance = MagicMock()

        bank_account_repo = MagicMock()
        bank_account_repo.get_by_account_id = MagicMock(
            return_value=saving_account)
        bank_account_repo.update = MagicMock()

        saving_interest_calculator = MagicMock()
        saving_interest_calculator.calculate_interest_from_balance = MagicMock(
            return_value=10)

        bank_account_use_cases = BankAccountUseCases(
            bank_account_repo, saving_interest_calculator)

        bank_account_use_cases.update_saving_account_with_saving_interest(
            account_id='103-117-446')

        bank_account_repo.get_by_account_id.assert_called_once_with(
            '103-117-446')

        saving_account.get_balance.assert_called_once()
        saving_interest_calculator.calculate_interest_from_balance.assert_called_once_with(
            1000)
        saving_account.set_balance.assert_called_once_with(1010)

        bank_account_repo.update.assert_called_once_with(saving_account)
