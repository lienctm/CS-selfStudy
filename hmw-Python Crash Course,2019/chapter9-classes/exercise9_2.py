# Start with your class from Exercise 9-1. Create three different instances from the class,
# and call describe_restaurant() for each instance.
class Restaurant:
    def __init__(self, restautant_name, cuisine_type, location):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type
        self.location = location

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is on {self.location}. Their {self.cuisine_type} is so great")

restaurant = Restaurant("Pho Ha Noi", "Vietnames noodle", 'San Jose')
restaurant.describe_restaurant()