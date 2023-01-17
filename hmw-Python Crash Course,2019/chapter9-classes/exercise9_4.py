# Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
# and then change this value and print it again.Add a method called set_number_served() that lets you
# set the number of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any num- ber you like that could represent how many customers were served in a day of business.
class Restaurant:
    def __init__(self, restautant_name, cuisine_type):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is on SF. Their {self.cuisine_type} is so great")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open")

    def set_number_served(self):
        print(f'The restaurant are serving {self.number_served} people')

    def increment_number_served(self, serving_number):
        self.number_served = serving_number

restaurant = Restaurant("Hayhay", "Mexican food")
restaurant.set_number_served()
restaurant.number_served = 15
restaurant.set_number_served()
restaurant.increment_number_served(30)
restaurant.set_number_served()
