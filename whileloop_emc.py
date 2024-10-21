'''i = 0
while (i<5):
    i += 1
    print(i)

i = 0
while (i < 200):
    i += 10
    print(i,end=",")

i = 11
while(i > 0):
    i -= 1
    print(i)

i = 6           #factorial using while loop
fact = 1
while(i > 0):
    fact *= i
    i -= 1
print(fact)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

one = 'engineering'
for i in one:
    if i == 'i':
        continue
    print(i)'''

for i in range(5):
    for j in (1,i+1):
        print(j,end='')
    print()