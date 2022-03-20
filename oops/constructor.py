# Constructor and self 
# size of the object depends upon the no of variable it is having
# 
class computer:
    # how to define variable inside an object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def calling(self):
        print("The name of the person is" ,self.name ,"and the age of the person",self.age)
    # Compare takes two parameter  :#1 who is calling #2 with whom to compare
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False



c1=computer("Richa",14)
c2=computer("Jina",13)

# id shows the address of the variable
print(id(c1))
print(id(c2))
c1.calling()
c2.calling()

# comparing here whether c1's age and c2's age is same or not
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")