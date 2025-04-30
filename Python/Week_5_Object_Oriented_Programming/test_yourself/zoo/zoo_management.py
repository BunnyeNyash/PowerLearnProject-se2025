''' Zoo management System '''

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    
    def describe(self):
        return f"{self.name} is a {self.__class__.__name__.lower()}"
    
    
    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Every animal must define its own")
    
    
    @abstractmethod
    def eat(self):
        pass    # Every animal to define its own


    def sleep(self):
        return f"{self.name} goes to sleep"



class Lion(Animal):
    def make_sound(self):
        return f"{self.name} says Roar"
    
    def eat(self):
        return f"{self.name} eats meat."

class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} says Trumpet"
    
    def eat(self):
        return f"{self.name} eats grass."

class Parrot(Animal):
    def make_sound(self):
        return f"{self.name} says Squawk"
    
    def eat(self):
        return f"{self.name} eats seeds."

animals = [Lion("Simba"), Elephant("Ndovu"), Parrot("Bunnye")]

for animal in animals:
    print(animal.describe())
    print(animal.make_sound())
    print(animal.eat())
    print(animal.sleep())
    print("\n")


