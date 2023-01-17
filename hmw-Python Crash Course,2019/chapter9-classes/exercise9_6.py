# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162)
# or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method
class Restaurant:
    def __init__(self, restautant_name, cuisine_type):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is on SF. Their {self.cuisine_type} is so great")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open")

class IceCreamStand(Restaurant):
    def __init__(self, restautant_name, cuisine_type):
        super().__init__(restautant_name, cuisine_type)
        self.flavors = ['strawberry', 'mint', 'mango', 'chocolate']

    def icecreamflavors(self):
        print('This restaurant has some icecream with flavors are:')
        for flavor in self.flavors:
            print(flavor)
        

restaurant = IceCreamStand('Momo', 'Taiwan food')
restaurant.describe_restaurant()
restaurant.icecreamflavors()
