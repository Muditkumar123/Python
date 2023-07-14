



class Student:
    name = None
    age=None
    address =None
    def __init__(self):
        self.name = "unknown"
        self.age =0
        self.address ="Not available"

    def setinfo(self,name,age):
        self.name = name
        self.age =age

    def setinfo(self,name,age,address):
        self.name = name
        self.age =age
        self.address = address

    def printInfo(self):
        print("Name:"+self.name)
        print(f"Age:{self.age}")
        print("Address:"+self.address)
        print("\n")
    

list=[]



for i in range(0,2):
    a=input("Input the name:")    
    b=int(input("Input the age:"))
    c=input("Input the Address:")
    student= Student()
    student.setinfo(a,b,c)
    list.append(student)

print(list[0].printInfo())
print(list[1].printInfo())
