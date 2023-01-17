from user import User

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
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