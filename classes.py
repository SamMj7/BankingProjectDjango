'''class laptop:
    def __init__(self):   
        self.prize = 0
        self.processor = ''
                                #intro for objects and classes
    def display(self):
        print('prize:',self.prize)
        print('processor:',self.processor)
hp = laptop()

hp.prize = 50000
hp.processor = 'i5'

hp.display()

class student:
    def __init__(self):
        self.name = 'Name'
        self.register = 'register'
    def display(self):                  # init and self -- constructor
        print("Name :", self.name)
        print("Register :", self.register)

s = student()
s.name = 'Sam'
s.register = 35
s.display()

class fruit:
    def __init__(self,color): 
        self.color = color
        #print(self.color)
apple = fruit('red')        #passing parameter (color)
print(apple.color)

class teacher:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def display(self):
        print("Name :",self.name)
        print("Regno :",self.regno)
t1 = teacher('sam',35)
t2 = teacher('ram',33)
t1.display()
t2.display()
'''
class calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b 
    def add(self):
        print("Addition : ", self.num1+self.num2) #if parameters are not passed
    def sub(self,a,b):
        print("Subtraction :", a-b)               #parameterized function
    def mul(self):
        print("Multiplication :", self.num1*self.num2)
    def div(self,a,b):
        print("Division :", a//b)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = calculator(a,b)
c.add()
c.sub(a,b)
c.mul()
c.div(a,b)