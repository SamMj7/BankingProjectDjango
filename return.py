'''s_username = 'emc'
s_password = 123
user = input("enter user name:")
pwd = int(input("enter a password:"))

def validate():
    if (s_username == user and s_password == pwd):
        return True
    else:
        return False
        
res = validate()
print(res)'''

a = int(input("enter a :"))
b = int(input("enter b :"))
c = 10
def add(n1,n2):
    return n1 + n2
res = add(a,b)
print(res)
print(res * c)
