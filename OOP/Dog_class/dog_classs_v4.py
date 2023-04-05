
class Dog:
    """ A python class to represent Dog"""
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        """ param:
            name: str
            age: int
            breed: str

            Creates an instance of the Dog class
"""
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        """ Give info about the instance"""
        return f"{self.name} is {self.age} years old and \
belongs to the breed {self.breed}"

    def __repr__(self):
        return f"Dog('{self.name}',{self.age}, '{self.breed}')"

    def speak(self, sound):
        """param:
            sound: str

            returns a str that represents how a dog barks
        """
        return f'{self.name} says {sound}'

    
  

    
