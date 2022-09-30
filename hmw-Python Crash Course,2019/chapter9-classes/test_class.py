#define a type of object using the class keyword
#classes require an initialization function, known as constructor
#in defining each method of an object, self should be its first paramater

class Student():
    # init method or constructor
    def __init__(self, name, id):
       self.name = name
       self.id = id
    def changeID(self, id):
        self.id = id
    def print(self):
        print ("{} - {}".format(self.name, self.id))

anna = Student("Anna", 8)
anna.print()
anna.changeID(10)
anna.print()
