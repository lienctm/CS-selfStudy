class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Setting a defaul value for an attribute
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """print a statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!")
    def increment_odemeter(self, miles):
        self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an attribute's value directly
my_new_car.odometer_reading = 30
my_new_car.read_odometer()

# Modifying an attribute through method
my_new_car.update_odometer(23)
my_new_car.read_odometer()

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75: 
            range = 260
        elif self.battery_size == 100: 
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attribute of the parent class."""
        super().__init__(make, year, model)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()