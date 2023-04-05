
# Parent class
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


    def __str__(self):
        """ Give info about the instance"""
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Dog('{self.name}',{self.age})"

    def speak(self, sound):
        """ sound: str

            returns a str that represents how a dog barks
        """
        return f'{self.name} says {sound}'

# Child Class
class JackRusselTerrier(Dog):
    
    def __repr__(self):
        return f"JackRusselTerrier('{self.name}',{self.age})"

# Child Class
class Bulldog(Dog):
    pass   
