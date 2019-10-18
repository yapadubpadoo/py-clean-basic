import unittest
from app.data_provider.mongodb_provider import MongoDBProvider


class TestMongoDBDataProvider(unittest.TestCase):
    def setUp(self):
        MongoDBProvider.__instance = None
        pass

    def test_create_mongodb_connection_with_same_uri_should_raise_error(self):
        with self.assertRaises(Exception) as e:
            m1 = MongoDBProvider(mongodb_uri="mongo-host-1")
            m2 = MongoDBProvider(mongodb_uri="mongo-host-1")

    def test_create_mongodb_connection_with_same_uri_should_be_ok(self):
        m1 = MongoDBProvider(mongodb_uri="mongo-host-1")
        m2 = MongoDBProvider(mongodb_uri="mongo-host-2")
