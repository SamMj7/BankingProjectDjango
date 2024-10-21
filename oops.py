class student: 

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    
    def __str__(self):
        return "s1-{} s2-{}".format(self.m1,self.m2)
    


s1 = student(60,70)
s2 = student(50,50)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)
print(s1)
print(s2)


class employee:
    def __init__(self, name : str, salary : int) -> None:
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self, name, salary, department : str) -> None:
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f" Name : {self.name} Salary : {self.salary} Dept : {self.department}")

m = manager('sam',40000,789)
m.display()