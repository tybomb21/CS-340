from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:47172' % ('Tyler', 'Admin'))
        self.database = self.client['AAC']
        self.animals = self.database['animals']

    def create(self, data):
        if data:
            result = self.animals.insert_one(data)
            return result.inserted_id
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, search_criteria=None):
        if search_criteria is None:
            search_criteria = {}
        return list(self.animals.find(search_criteria))

# Example usage
animal_shelter = AnimalShelter()
animal = {
    "name": "Max",
    "species": "Dog",
    "breed": "Labrador Retriever",
    "age": 3,
    "gender": "Male",
    "weight": 70
}
animal_id = animal_shelter.create(animal)
print(f"Created animal with ID: {animal_id}")
animals = animal_shelter.read({"species": "Dog"})
print(f"Found {len(animals)} dogs")
