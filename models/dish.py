from configs.db import db

class Dish:
    collection = db['dishes']  # Collection name for dishes

    def __init__(self, dish_name, price, availability):
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def save(self):
        # Save the dish to the database
        self.collection.insert_one({
            'dish_name': self.dish_name,
            'price': self.price,
            'availability': self.availability
        })

    def update(self):
        # Update the dish in the database
        self.collection.update_one(
            {'_id': self._id},
            {'$set': {
                'dish_name': self.dish_name,
                'price': self.price,
                'availability': self.availability
            }}
        )

    def delete(self):
        # Delete the dish from the database
        self.collection.delete_one({'_id': self._id})

    @staticmethod
    def get_all():
        # Retrieve all dishes from the database
        return list(Dish.collection.find())

    @staticmethod
    def get_by_id(dish_id):
        # Retrieve a dish by its ID from the database
        return Dish.collection.find_one({'_id': dish_id})
