
#Public
#Protected
#Private


class Human:
    name: str
    __age: int
    def __init__(self, v_name='Vasya'):
        self.name = v_name
        self._password = "12345"
        self.__age = 30


    def get_age(self):      #getter    #dlya privatnogo ispolzovaniya
        return self.__age

    def set_age(self, v_age: int):  #setter      #dobovleniie cifri dlya privatnogo ispolzovaniya
        if type(v_age) == int:
            self.__age = v_age
        else:
            raise TypeError


o_vasya = Human()
print(o_vasya.name)
#print(o_vasya.__age)
print(o_vasya._password)
print(o_vasya.get_age())

print(f'age = {str(o_vasya.get_age())}')

o_vasya.set_age(40)
print(o_vasya.get_age())