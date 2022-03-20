# types of Variables
# -Class Variable
# -Instance Variable
# -Static Variable-where class and static are same


class car:
    # When we define a variable outside of init it becomes a class variable
    price=20000000


    def __init__(self):

        # These are Instance Variable
        self.mil=10
        self.company="BMW"



c1=car()
c2=car()

c1.mil=8
# class varables can get access with class name
car.price=2800000
print(c1.company,c1.mil,c1.price)
print(c2.company,c2.mil,c2.price)
