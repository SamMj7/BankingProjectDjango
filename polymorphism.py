'''class Animal():     
    def Sound(self):
        print("Animal makes sound.")
class dog(Animal):
    def Sound(self):            #method overriding
        print("Dog walks.")
class bird(Animal):
    def Sound(self):        #same function used for different types 
        print("Bird Sings.")
a1 = bird()
a1.Sound()

class shape():
    def area(self):
        return 0 
class rectangle(shape):
    def area(self):
        l = 10
        b = 20
        return (l*b)
s = rectangle()
print(s.area())

class person():
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,grade,name):
        self.grade = grade
        super().__init__(name)
    def display(self):
        print(self.name,self.grade)
        
d = student('A','sam')
d.display() 

class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
c = car()
c.start() '''

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)   #initializing parent class
        self.department = department
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
m = manager('sam',50000,'Mech')
m.display()