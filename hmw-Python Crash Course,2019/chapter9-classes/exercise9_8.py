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

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges == 'add' :
            print("You can add a post!")
        elif self.privileges == 'delete':
            print("You can delete a post!")
        else :
             print("You can ban user!")
my_admin = Privileges('')
my_admin.show_privileges()
