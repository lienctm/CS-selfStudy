# Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 100 if it isn’t already. 
# Make an electric car with a default battery size, call get_range() once, and then call get_range()
# a second time after upgrading the battery. You should see an increase in the car’s range.
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

class Battery:
    def __init__(self, battery_size = 55):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self, battery):
        self.battery_size += battery

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
my_tesla.battery.upgrade_battery(25)
my_tesla.battery.get_range