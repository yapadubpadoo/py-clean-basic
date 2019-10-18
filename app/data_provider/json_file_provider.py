import json


class JSONFileProvider:
    def __init__(self, path):

        try:
            self.json_file = open(path, "r")
            self.data = json.load(self.json_file)
            self.json_file.close()
        except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
            print("ERROR", e)
            self.data = {
                'accounts': []
            }

        # re-open for writing
        self.json_file = open(path, "w")

    def find_one(self, condition):
        filter_keys = list(condition.keys())
        print(filter_keys)
        print(filter_keys[0])
        print(condition[filter_keys[0]])
        print(self.data['accounts'])
        for account in self.data['accounts']:
            if account[filter_keys[0]] == condition[filter_keys[0]]:
                return account

    def insert_one(self, bank_account):
        print(self.data['accounts'])
        self.data['accounts'].append(bank_account.__dict__)
        json.dump(self.data, self.json_file, indent=4)

    def update_one(self, filter_condition, update_condition):
        updated_item = update_condition["$set"]
        count = 0
        for account in self.data['accounts']:
            if account['account_id'] == updated_item.get_account_id():
                self.data['accounts'][count] = updated_item.__dict__
            count = count + 1
        json.dump(self.data, self.json_file, indent=4)
