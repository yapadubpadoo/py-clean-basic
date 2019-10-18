import pymongo


class MongoDBProvider:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDBProvider.__instance != None:
            return MongoDBProvider.__instance

    def __init__(self, mongodb_uri):
        if MongoDBProvider.__instance != None \
                and MongoDBProvider.__instance.mongodb_uri == mongodb_uri:
            raise Exception("Object already created")
        else:
            self.mongodb_uri = mongodb_uri
            self.connection = pymongo.MongoClient(mongodb_uri)
            MongoDBProvider.__instance = self
