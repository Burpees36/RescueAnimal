from pymongo import MongoClient
from pymongo.errors import PyMongoError
import urllib.parse


class AnimalShelter(object):
    """ CRUD operations for the Animal collection in MongoDB """

    def __init__(self, username, password):
        """
        Initialize the MongoDB client connection and authenticate
        using credentials from Apporto

        Connection Variables
        """
        USER = urllib.parse.quote_plus(username)
        PASS = urllib.parse.quote_plus(password)
        # USER = 'aacuser'
        HOST = 'nv-desktop-services.apporto.com'
        # PASS = 'password1'
        PORT = 34100
        DB = 'AAC'
        COL = 'animals'


        # Initialize Connection

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

    def create(self, data):
        """
        Insert a document into the collection.
        """
        try:
            if isinstance(data, dict):  # Verify data is dictionary
                self.collection.insert_one(data)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    def read(self, query):
        """
        Returns a list of matching documents, or empty list.
        """
        try:
            if isinstance(query, dict):  # Verify data is dictionary
                results = self.collection.find(query)
                return list(results)  # makes results a list
            else:
                return []  # return empty list if no results found
        except Exception as e:
            print(f"Error reading documents: {e}")
            return []

    def update(self, query, new_data):
        """
        Update documents found in query with new_data.
        """
        try:
            if isinstance(query,dict) and isinstance(new_data, dict):
                result = self.collection.update_many(query, {"$set": new_data})
                return result.modified_count
            else:
                return 0
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

    def delete(self, query):
        """
        Delete documents that match the query
        """
        try:
            if isinstance(query, dict):
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0
