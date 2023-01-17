# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
# Write a method called increment_login _attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.

class User:
    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country
        self.login_attempts = 0

    def read_login_attempts(self):
        full_name = f'{self.first_name} {self.last_name}' 
        print(f'{full_name} is trying to login {self.login_attempts} times')

    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}' 
        print(f'Hello {full_name}')

    def increment_login_attempts(self, increase_times):
        self.login_attempts += increase_times

    def reset_login_attempts(self, decrease_times):
        if self.login_attempts < decrease_times :
            print(f"Error, {self.first_name} is trying to login only {self.login_attempts} times")
        else:
            self.login_attempts -= decrease_times

user = User("Kim", "Dong", '18','female', 'The US')
user.greet_user()
# Print the value of login_attempts to make sure it was incremented properly
user.increment_login_attempts(3)
user.read_login_attempts()
user.increment_login_attempts(5)
user.read_login_attempts()
# Print login_attempts again to make sure it was reset to 0.
user.reset_login_attempts(4)
user.read_login_attempts()
user.reset_login_attempts(3)
user.read_login_attempts()
user.reset_login_attempts(2)

