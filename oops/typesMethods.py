# Types of Methods
# -Instance Method
# -Class Method
# -Static Method
# from locale import MON_2


# from distutils.log import info


class student:
    # This is a class method
    @classmethod   # this is decorator
    def info(cls):
        return cls.school



    # these are instance methods
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2 
        self.m3=m3 
    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def getM1(self):
        return self.m1
    def getM2(self):
        return self.m2
    def getM2(self):
        return self.m3

s1=student(35,37,38,"Bhatnagar")
s2=student(25,34,31,"kv")
# print(s1.m1)
print(s1.avg())

# this is mutator 
print(s1.getM1())
# calling info
print(student.info())


# instance method types
# Accessor-only fetching the value
# Mutators-if you want   to modify the value