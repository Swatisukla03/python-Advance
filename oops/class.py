# Class is a deign or blueprint of any of the object.
# Without designing the class we cann't make objects.

class computer:

    def __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram

    def config(self):
        print("config is",self.cpu,self.ram)

# Different types of classes have different objects ,but different objects have the same class.

# a="8"
# print(type(a))
# Here it shows every object has it's own values
comp1=computer('i5',16)
comp2=computer('Ryzan 3',8)
# print(type(comp1))
# computer.config(comp1)
# comp1.config()
comp1.config()
comp2.config()

