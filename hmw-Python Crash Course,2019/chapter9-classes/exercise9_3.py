# Make a class called User. Create two attributes called first_name and last_name, and then create
# several other attributes that are typically stored in a user profile. Make a method called describe_user()
# that prints a summary of the user’s information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country

    def describe_user(self):
        full_name = f'{self.first_name} {self.last_name}' 
        print(f'Hello, My name is {full_name}. I am a {self.gender}. I am {self.age} years old, and lives in {self.country}')

    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}' 
        print(f'Hello {full_name}')

user = User('Anna', 'Truong', '22', 'female', 'France')
user.greet_user()
user.describe_user()
user1 = User('Ken', 'Ford', '45', 'Male', 'Italia')
user1.greet_user()
user1.describe_user()
