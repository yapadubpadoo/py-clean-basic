from app.entities.saving_account import SavingAccount


class BankAccountRepo:
    def __init__(self, account_data_provider, account_id_provider):
        self.account_data_provider = account_data_provider
        self.account_id_provider = account_id_provider

    def create(self, name, lastname, initial_balance):
        account_id = self.account_id_provider.get_next()
        new_saving_account = SavingAccount(
            account_id, name, lastname, initial_balance)
        self.account_data_provider.create_one(new_saving_account)
        return new_saving_account

    def get_by_account_id(self, account_id):
        account_data = self.account_data_provider.get_one_by_account_id(
            account_id)
        return SavingAccount(
            account_id=account_data['account_id'],
            name=account_data['name'],
            lastname=account_data['lastname'],
            balance=account_data['balance']
        )

    def update(self, bank_account):
        self.account_data_provider.update_one(bank_account)
