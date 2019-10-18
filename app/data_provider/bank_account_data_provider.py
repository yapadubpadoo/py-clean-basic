from app.data_provider.mongodb_data_provider import MongoDBDataProvider


class BankAcccountDataProvider(MongoDBDataProvider):
    def find_one(self, condition):
        self.connection.collection.find(condition)

    def insert_one(self, bank_account):
        self.connection.collection.insert_one(back_account)

    def update_one(self, filter_condition, updated_bank_account)
    self.connection.collection.update(filter_condition, )
