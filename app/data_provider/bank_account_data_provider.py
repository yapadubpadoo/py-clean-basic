
class BankAcccountDataProvider():

    def __init__(self, collection):
        self.collection = collection

    def get_one_by_account_id(self, account_id):
        return self.collection.find_one({"account_id": account_id})

    def create_one(self, bank_account):
        self.collection.insert_one(bank_account)

    def update_one(self, updated_bank_account):
        account_id = updated_bank_account.get_account_id()
        filter_condition = {"account_id": account_id}
        updated_condition = {"$set": updated_bank_account}
        self.collection.update_one(filter_condition, updated_condition)
