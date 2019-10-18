from app.entities.saving_account import SavingAccount


class BankAccountRepo:
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def create(self, bank_account):
        self.data_provider.insert_one(bank_account)

    def get_by_account_id(self, account_id):
        account_data = self.data_provider.find_one(
            {'account_id': account_id})
        return SavingAccount(account_data.account_id, account_data.identity_number, account_data.name, account_data.lastname, account_data.balance)

    def update(self, bank_account):
        self.data_provider.update_one(
            {'account_id': bank_account.account_id}, bank_account)
