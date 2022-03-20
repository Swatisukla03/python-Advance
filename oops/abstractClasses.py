# Abstract class
# abc-abstractbaseClasses
#Abstract Methods Only have the declaration but no defination
# this acts as the blueprint for other classes and creates a set of methods that are must to be created within any child classes built from the abstract class.


from abc import  ABC,abstractmethod


class comp(ABC):
    @abstractmethod
    def process(self):
        # print("Running")
        pass

class laptop(comp):
    def process(self):
      pass

lap=laptop()

# comp1=comp()
# comp1.process()


# EXAMPLE 2
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Triangle(polygon):
    def sides(self):
        print("I have 3 sides")


class rectangle(polygon):
    def sides(self):
        print("I have 4 sides")

class hexagon(polygon):
    def sides(self):
        print("I have 6 sides")

tri=Triangle()
tri.sides()
rect=rectangle()
rect.sides()
hex=hexagon()
hex.sides()



# Example 3

from abc import ABC,abstractmethod


class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")


class snake(animal):
    def move(self):
        print("I can only crawl")


class dog(animal):
    def move(self):
        print("I can bark")


h=human()
h.move()
s=snake()
s.move()
d=dog()
d.move()




