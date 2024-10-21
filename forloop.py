'''for i in range(1,11):
    print(i,"x 3 =",i*3)
for i in range(1,11):
    if (i % 2 ==0):      #print even numbers from 1 to 10
        print(i)
sum = 0
for i in range(1,11):
    if i % 2 == 0:     #count the number of even numbers between 1 to 10
        sum += 1
print(sum)

e_sum = 0
o_sum = 0
for i in range(1,11):
    if i % 2 == 0:
        e_sum += 1
    else:              #count the odd and even numbers between 1 to 10
        o_sum += 1
print("even-",e_sum)
print("odd-", o_sum)

sum = 0
for i in range (1,100):  #count the nos divisible by 3 and 5 between 1 to 100
    if (i%3 == 0) and (i%5 ==0):
        sum += 1
print("Numbers divisible by 3 and 5 -",sum)

a = []
print("Enter 'n' numbers:")
n = int(input("Enter a number :"))
for i in range(n):
    num = int(input("Enter num:"+ str(i+1)))
    a.append(num)
print(a)
sum = 0             #Find the sum and average of 10 numbers
for i in a:
    sum += i
print("sum is :",sum)
print("Avg is :", sum/n)


for i in range(1,6): #cube for 5 numbers
    cube = (i*i*i)
    print("Number is:",i,"and the cube of Number",i,"is",cube)

#Nested for loop
for i in range(1,6):
    for j in range(1,4):
        print(j,'apple')

for w in range(1,3):
    print("Week:",w)
    for d in range(1,4):
        print("day:",d)'''


for i in range(1,6):
    print()
    for j in range(i-1,6):
        j = 5 - j
        if j == 0:
            break
        print(j,end="")


