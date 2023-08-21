from pymongo import MongoClient

class CRUD(object):
    """ CRUD operations for MongoDB database """

    def __init__(self, username, password, host, port, db_name, collection_name):
        # Initializing the MongoClient and connecting to the specified MongoDB database and collection.
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/')
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def insert_document(self, data):
        """Inserts a document into the specified MongoDB collection."""
        if data is not None:
            result = self.collection.insert_one(data)  # data should be a dictionary
            return True if result.inserted_id else False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def query_documents(self, lookup_query):
        """Queries for documents from the specified MongoDB collection."""
        if lookup_query is not None:
            cursor = self.collection.find(lookup_query)
            return list(cursor)
        else:
            raise Exception("Lookup query parameter is empty, provide key/value lookup pair")
           
    def update_documents(self, lookup_query, update_data):
        """Updates document(s) in the specified MongoDB collection."""
        if lookup_query and update_data:
            result = self.collection.update_many(lookup_query, {"$set": update_data})
            return result.modified_count
        else:
            raise Exception("Lookup query or update data is empty, provide key/value pairs")

    def delete_documents(self, lookup_query):
        """Deletes document(s) from the specified MongoDB collection."""
        if lookup_query:
            result = self.collection.delete_many(lookup_query)
            return result.deleted_count
        else:
            raise Exception("Lookup query is empty, provide key/value lookup pair")