#Access modifiers
#private - variable can be accessed only within the class. (eg) 'self.__sam' (double underscore)
#protected - variable can be accessed within sub classes(derived class). (eg) 'self._sam' (single underscore)
#public - Accessible from outside the class.

class Company():
    def __init__(self,name,type,charger):
        self.__name = name   #private _ _
        self._type = type    #protected _
        self.charger = charger
    def Com(self):
        print(self.__name)
class Title(Company):
    def Display(self):
        print(self._type)
        print(self.charger)
c = Company('Apple','Friendly','C type')
t = Title('Apple','Friendly','C type')
#t.Display()
print(t._type)
c.Com()
