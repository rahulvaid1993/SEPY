# classes are user defined blueprint or prototype
# if functions are wrapped in a class then they are called as Methods
# if you do not define any constructor then default constructor would be called
# whenever you create an object of a class then the constuctor code is executed
#There are two types of variables 1. class 2. instance
#instance variable change with obj creation
#Self keyword is mandatory for object creation
#constructor has to be assigned as __init__



class Calculator:
    num = 100

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('I am called when obj is created')



    def getdata(self):
        print('i am a method')

    def sum(self):
        return self.a+self.b+self.num


obj = Calculator()
print(obj.getdata())
