from pymongo import MongoClient
class MongoClientHelper:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = None

    def connect(self, db_name: str):
        """Connect to the specified database."""
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        """Get a collection from the connected database."""
        if self.db is None:
            raise Exception("Database not connected. Call connect() first.")
        return self.db[collection_name]
    
    def ping_db(self):
        """Ping the database to check if the connection is alive."""
        if self.db is None:
            raise Exception("Database not connected. Call connect() first.")
        return self.client.admin.command('ping')
    
    def close(self):
        """Close the MongoDB connection."""
        self.client.close()
        self.db = None
