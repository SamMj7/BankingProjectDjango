class phone:
    def __init__(self,brand,prize,chargertype):
        self.brand = brand
        self.prize = prize                          #instance_variable = self.____
        self.chargertype = chargertype
    def display(self):
        print("brand",self.brand)
        print('Prize',self.prize)
        print('Type', self.chargertype)
p = phone('samsung',50000,'d-type')
p.display()

class phone:
    chargertype = 'c-type'                  #class_variable
    def __init__(self,brand,prize):
        self.brand = brand
        self.prize = prize                          
    def display(self):
        print("brand:",self.brand)
        print('Prize:',self.prize)
        print('Type:', self.chargertype)

phone.chargertype = 'b-type' 
p = phone('samsung',50000)
p.display()