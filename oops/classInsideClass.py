# INNER CLASS


from io import BufferedRandom
from unicodedata import name
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


class student:
    def __init__(self,name,rollno,laptop):
        self.name=name
        self.rollno=rollno 
        self.laptop=laptop


    def show(self):
        print(self.name,self.rollno)
        self.laptop.show()

#  this is an Inner class where we are using a class inside another class
# here the laptop class will be a variable of the main class 

    class laptop:

        def __init__(self,brand,cpu,ram):
            self.brand=brand 
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(self.brand,self.cpu,self.ram)


# initializing the laptop class
l1=student.laptop()
s1=student("Swati",23,"HP","i5",16)
s2=student("Ayush",13,"Dell","i7",8)


s1.show()
