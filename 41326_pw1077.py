#Parker Wood
#4/13/26

"""SYNTAX for OOP:
class class_name:
    documentation string
    variables: instance variable, static variable, and local variable
    methods: behavior or instance method, static method, class method
    """
"""
class Student:
    #This is a student class with nessesary data
    def __init__(self):
        self.name="Sam"
        self.age = 20

    def talk(self):
        print("Hello")
        print("Class")
        print("Welcome To")
        print("OOPs")

s1 = Student()
print(s1.name) #Calling on the .name property from the class
print(id(s1)) #Prints the memory number
#print(Student.__doc__) #This will run all of the documents in the student class

s2 = Student()
print(s2.name)
print(id(s1)) #Different memory number
s2.talk()
"""

class Student:
    #This is a student class with nessesary data
    def __init__(self,name,age): #The __init__ is made for constructors
        self.name = name
        self.age = age

    def talk(self):
        print("Hello ", self.name)
        print("Class")
        print("Welcome To")
        print("OOPs at the age of: ", self.age)

s1 = Student("Bob", 21)
s2 = Student("Tim", 23)

print(id(s1))
print(s1.name)
s1.talk()

print(id(s2))
print(s2.name)
s2.talk()
