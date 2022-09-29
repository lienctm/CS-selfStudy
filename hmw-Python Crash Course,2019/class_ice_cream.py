class IceCreamStand:
    def __init__(self, name, flavors, prices):
        self.name =  name
        self.flavors = flavors
        self.prices = prices
    def get_ice_cream(self):
        order = f"Ice cream : {self.name}, flavors: {self.flavors}, price : ${self.prices}. "
        return order
my_ice_cream = IceCreamStand('blue sky', 'blueberry', '5')
print(my_ice_cream.get_ice_cream())
    
