class Admin:
    def __init__(self,name, privileges):
        self.name = name
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges == 'add' :
            print(f"{self.name} : You can add a post!")
        elif self.privileges == 'delete':
            print(f"{self.name} : You can delete a post!")
        else :
             print(f"{self.name} : You can ban user!")
my_admin = Admin('Hanna', '')
my_admin.show_privileges()




        
       