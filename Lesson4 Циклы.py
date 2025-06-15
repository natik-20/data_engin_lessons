
l1 = [1,2,3,4,5,6,7,8,9]

v_sum = 0
for one_element in l1:
    if one_element % 2 == 0:
        v_sum += one_element
#print(one_element)

#print(v_sum)


l2 = [30,40,50]

v_sum = 0
for one_element in l1:
    v_sum = v_sum + one_element

#print(v_sum)

#for i in l2:
    #print(i)
    #print(i *10)

d1 = {
    'one': l1,
    'two': l2
}

#print(d1)

#for one_key in d1.keys():
 #   print(one_key, d1.get(one_key))

i = 1
d2 = dict()

#for one_element in l1:
   # d2[i] = one_element
   # i = i + 1

#print(d2)

i = 0
import time

#for one_element in [1,2,3]:
 #   for i in [1,2,3,4,5]:
        #print(f'one_element + {str(one_element)}')
        #print('Selena balam', i)
        #i += 1
        #time.sleep(1)


i = 1
while True:
    print ('Selena', i)
    i += 1
    if i > 10:
        break
    #time.sleep(1)





