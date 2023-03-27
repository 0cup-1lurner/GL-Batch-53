
class Dog:
    """ A python class to represent Dog"""
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        """ param:
            name: str
            age: int

            Creates an instance of the Dog class
"""
        self.name = name
        self.age = age

##    def __str__(self):
##        """ Give info about the instance"""
##        return f"{self.name} is {self.age} years old."
##
    def __repr__(self):
        return f"{self.name} is {self.age} years old"
  

    
