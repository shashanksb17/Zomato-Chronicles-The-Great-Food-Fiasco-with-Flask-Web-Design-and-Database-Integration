from mongoengine import Document, StringField, FloatField, IntField, ListField


class Dish(Document):
    dish_name = StringField(required=True)
    price = FloatField(required=True, min_value=0)
    availability = StringField(required=True)
    ratings = ListField(IntField(min_value=1, max_value=5), default=[])
    reviews = ListField(StringField(), default=[])

    def add_rating(self, rating):
        self.ratings.append(rating)

    def add_review(self, review):
        self.reviews.append(review)

    def calculate_average_rating(self):
        total_ratings = sum(self.ratings)
        average_rating = total_ratings / len(self.ratings) if self.ratings else 0
        return round(average_rating, 1)

    def save(self, *args, **kwargs):
        self.average_rating = self.calculate_average_rating()
        return super(Dish, self).save(*args, **kwargs)
