

def func1():
    print('a')
    print('b')

#for one_element in range(1,11):
#    func1()


def func2(local_element):
    print(local_element, local_element*2)

for one_element in [1, 2, 3]:
    func2(local_element=one_element)

def func3(name, surname):
    print(f'name is {str(name)}, surname is {str(surname)}')

func3(name = 'Selena', surname = 'Talibova')

def sum2 (a, b):
    result = a + b
    return result
print(sum2(a=1,b=2))

def sum3(a,b,c):
    return a+b+c

print(sum3(a=100, b=30, c=60))

def any_function(a, b):
    result1 = a+b
    result2 = a-b
    return result1, result2
varl1, varl2 = any_function(10,8)
#print(varl1)
#print(varl2)

def func123(a: int):
    return  a*2

#def func123(a: str):
#    return  a

#print(func123(a='Selena'))


def loop1():
    for element in range(10):
        print(element)
        if element > 5:
            return None
loop1()