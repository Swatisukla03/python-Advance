# Polymorphism -one thing can take many forms   
# -Duck typing
#  Eg in Polymorphism\


# Inbuilt function
print(len("Namaste Bharat"))
print(len([12,34,4,54,6,7.2,"Derniya"]))


# Example of user defined polymorphic functions
def add(x,y,z=0):
    return x+y+z
print(add(2,19))
print(add(12,3.5,6))

# Polymorphism with the class methods
class India():
    def capital(self):
        print("New DElhi is the Capital of India")

    def language(self):
        print("Hindi is the mostly spoken language in India")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington DC is the capital of America")

    def language(self):
        print("English is the widely spoken language at USA")

    def type(self):
        print("USA is considered under the developed Nation")



obj_India=India()
obj_India.language()
obj_India.type()
obj_India.capital()

print('\n')


# here it is the object of Usa class
obj_USA=USA()
obj_USA.language()
obj_USA.capital()
obj_USA.type()


print('\n')

for country in (obj_USA,obj_India):
    country.capital()
    country.language()
    country.type()


    # POLYMORPHISM with Inheritance

class bird:
    def intro(self):
        print("There are Many types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")

class sparrow(bird):
    def flight(self):
        print("These animals cann't fly")

class Ostrich(sparrow):
    # def flight(self):
        pass
obj_bird=bird()
obj_sparrow=sparrow()
obj_ostrich=Ostrich()
print('\n')

print("this is the features of Ostrich")
obj_bird.intro()
obj_bird.flight()

print('\n')
print("This is the characterstics og sparrow")
obj_sparrow.intro()
obj_sparrow.flight()

print('\n')
print("This is the characterstics of Ostrich")
obj_ostrich.intro()
obj_ostrich.flight()
