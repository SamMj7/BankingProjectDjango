'''class dad():
    def phone(self):
        print("dad's phone")
class mom():
    def sweet(self):
        print("mom's sweet")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")
ram = son()
ram.phone()   #single inheritance
ram.sweet()   #multiple inheritance

class grandpa():
    def phone(self):
        print("grandpa's phone")
class dad(grandpa):
    def lap(self):
        print("dad's laptop")
class son(dad):
    def money(self):
        print("son's money")
s = son()
s.lap()
s.phone()       #multilevel inheritance

class a():
    def __init__(self):
        print("A")
    def display(self):     #superfunction
        print("You are in class A")
class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in class B")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in class C")
c1 = c()
c1.display()'''

class parent_class:
    def father(self)-> None:
        print('Hi, I am the father.')

class parent_class2:
    def Mother(self)-> None:
        print('Hi, I am the Mother.')

class child_class(parent_class,parent_class2):
    def son(self)-> None:
        print("I am their son, Ram.")

c1 = child_class()
c1.father()
c1.Mother()
c1.son()

class Parent1:
    def greet(self)-> None:
        print("I am the GrandFather.")
class Parent2(Parent1):
    def Introduction(self)-> None:
        print("I am the Father.")
class Child(Parent2):
    def welcome(self)-> None:
        print(f'Welcome from GrandSon.')
c = Child()
c.welcome()
c.greet()
c.Introduction()

class base_class:
    def mom(self)-> None:
        return "home maker"
    
class derived_class(base_class):
    def son(self)-> None:
        return 'First born'
    
class derived_class2(base_class):
    def daughter(self)-> None:
        return 'Fav child'
d = derived_class2()
s = derived_class()
print(d.mom())
print(d.daughter())
print(s.son())
print(s.mom())