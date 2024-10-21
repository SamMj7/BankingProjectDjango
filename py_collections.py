'''a=[1,2,3,4,5]
b=[11,12,13]
a.pop()
a.insert(5,7)
a[2]=9
a.extend(b)
print(a)

a={1,2,3,4}
b={5,6}
a.update(b)
print(a)'''

a={ 'name':'ram',
    'age':21,
    'dob':1997
    }
#x = a['age']
#y = a.get('dob')    #access items
#print(a)
#print(x)
#print(y)
#print(a.keys())

#a['name']='sam'
#a.update({'dob':1993}) #change items
#print(a['name'])
#print(a)

#a['name']='jon'
#a.update({'color':'blue'})   #add items
#print(a)

#a.pop('name')
#a.popitem()     #remove items
#a.clear()
#print(a)

#for i in a.keys():
#for i in a.values():  #loop dictionaries
#for i,j in a.items():
 #   print(i,j)

a = {'name':'ram','year':'1997'}
b = {'name':'sam', 'year':'1993'}
c = {'name':'jon', 'year':'1996'}

d = {'a': a, 'b': b, 'c':c}

for i, j in d.items():      #looping through nested dictionaries
    print(i)
    for k in j:
        print(j[k])
