# An administrator is a special kind of user. Write a class called Admin that inherits from the User class
# you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method

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

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, country):
        super().__init__(first_name, last_name, age, gender, country)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'{self.first_name}, you are an admin. You can {privilege}')

kim = Admin('Kim', 'Vultano', '35', 'female', 'Germany')
kim.greet_user()
kim.show_privileges()

        