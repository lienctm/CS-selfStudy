class Restaurant:
    def __init__(self, restautant_name, cuisine_type):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is on SF. Their {self.cuisine_type} is so great")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open")