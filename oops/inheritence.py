

# Here A is SuperClass
# In this case we will see that subclass will find the init in itself first then it will go further to it's superClass
class A:
    def __init__(self):
        print("init A init")
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


# Here B is SubClass

class B:
    def __init__(self):
        super().__init__()   # this will call the initt of the superclass
        print("B in init")

    def feature3(self):
        print("Feature 3 is working")


    def feature4(self):
        print("Feature 4 is working")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

# class C(B):
#     def feature5(self):
#         print("Feature 5 is working")

a1=C()
# a1.feature1()
# a1.feature2()
# Here we can even access the features of Class A

# b1=B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# THis is MultiLevel Inheritance
# c1=C()
# c1.feature3()
# c1.feature1()


