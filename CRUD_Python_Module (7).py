from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username='aacuser', password='Password123!'):
        # Connection details
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Connect to MongoDB
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """Add a new animal to the database"""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Insert failed:", e)
                return False
        else:
            return False

    def read(self, query):
        """Get animals from the database"""
        if query is not None:
            data = self.collection.find(query, {"_id": False})
            return list(data)
        else:
            data = self.collection.find({}, {"_id": False})
            return list(data)
            
    def update(self, query, new_values):
        """Update existing animals"""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, new_values)
                return result.modified_count
            except Exception as e:
                print("Update not successful:", e)
                return 0
        else:
            return 0

    def delete(self, query):
        """Remove animals from the database"""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete failed:", e)
                return 0
        else:
            return 0