

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Selena']
#print(list1)
#print(list1[10])

list2 = [1, 1, 2, 2, 3, 4, 5, 'Selena']
#print(list2)


list2 = list(set(list2)) #Unikalnie znaceniya
#print(list2)


d1 = dict()
#print(d1)

d1['first'] = 1
d1['second'] = 2

#print(d1)

d1['selena'] = 'balam'
#print(d1)

#print(d1.get('selena'))
#print(d1.get('selen')) # tip none (kogda net takogo znacheniya)

l1 = list()
l1 = [1, -2, 3, 4, -5, 6, 7, 8, 9, 10, 'Selena']
#print(l1)
#print(l1[7])

d2 = {
    'first': 1,
    'second': 2,
    'third': 3,
}

#print(d2)
#print(d2.get('second'))

#print(d2.keys())
#print(d2.values())
#print(d1.pop('selena'))

d3 = dict()
d3['new'] = d2
d3['old'] = None

#print(d3)

#print(d3.get('new').__getitem__('second'))
#print(d3.get('new').get('second'))

list3 = list1 + list2
print(list3)

list3 = list1[4]*list2[3]
print(list3)
print(list1[4]*15)

s2 = {
    "val1": 1,
    "val2": 2,
    "val3": 'Selena balam',
    id: ['test', None, True, 1.3]
}

print(s2)

