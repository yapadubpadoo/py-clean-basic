import pymongo


class MongoDBDataProvider:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDBDataProvider.__instance != None:
            return MongoDBDataProvider.__instance

    def __init__(self, mongodb_uri):
        if MongoDBDataProvider.__instance != None \
                and MongoDBDataProvider.__instance.mongodb_uri == mongodb_uri:
            raise Exception("Object already created")
        else:
            self.mongodb_uri = mongodb_uri
            self.connection = pymongo.MongoClient(mongodb_uri)
            MongoDBDataProvider.__instance = self
