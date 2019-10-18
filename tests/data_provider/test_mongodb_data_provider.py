import unittest
from app.data_provider.mongodb_data_provider import MongoDBDataProvider


class TestMongoDBDataProvider(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_mongodb_connection_with_same_uri_should_raise_error(self):
        with self.assertRaises(Exception) as e:
            m1 = MongoDBDataProvider(mongodb_uri="mongo-host-1")
            m2 = MongoDBDataProvider(mongodb_uri="mongo-host-1")

    def test_create_mongodb_connection_with_same_uri_should_be_ok(self):
        m1 = MongoDBDataProvider(mongodb_uri="mongo-host-1")
        m2 = MongoDBDataProvider(mongodb_uri="mongo-host-2")
