import unittest
from unittest.mock import MagicMock
from app.data_provider.bank_account_data_provider import BankAcccountDataProvider


class TestBankAccountDataProvider(unittest.TestCase):
    def setUp(self):
        pass

    def test_update_one(self):
        collection = MagicMock()
        collection = MagicMock()
        collection.update_one = MagicMock()
        bank_account_data_provider = BankAcccountDataProvider(collection)

        updated_bank_account = MagicMock()
        updated_bank_account.get_account_id = MagicMock(
            return_value='111-222-33')

        filter_condition = {"account_id": '111-222-33'}

        bank_account_data_provider.update_one(updated_bank_account)

        collection.update_one.assert_called_once_with(
            filter_condition, {"$set": updated_bank_account})
