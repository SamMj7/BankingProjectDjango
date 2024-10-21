class Laptop:
    ChargerType = 'c-type'
    def __init__(self):
        self.brand = ''
        self.prize = 40 
    def setprize(self,prize)-> None:
        self.prize = prize
    def getprize(self):                     # instance_method (using self.***)
        print(self.prize)
    @classmethod
    def ChangedChargerType(cls):           #class_method (using decorators i.e @classmethod)
        cls.ChargerType = 'b-type'
        print('chagertype changed to b')
    @staticmethod
    def info():                             #staic_method
        print('Laptop is Hp')
hp = Laptop()
hp.setprize(20000)
hp.getprize()
hp.ChangedChargerType()
hp.info()