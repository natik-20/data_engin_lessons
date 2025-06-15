

class Human:
    hands = int
    foots = int
    head = int
    eyes = int
    age = int
    sex = int
    name = str

    def __init__(self, v_name):
        self.name = v_name
        self.hands = 2
        self.foots = 2
        self.head = 1
        self.eyes = 2
        self.age = 30
        self.sex = 1


    def mobilize(self):
        if self.sex == 1:
            self.hands = self.hands/2
            self.foots = self.foots/2
            self.eyes = self.eyes/2

    def see_info(self):
        print(f'name: {self.name}')
        print(f'hands = {int(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'head = {str(self.head)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

    def __str__(self):
        return f'name {self.name}' + '  ' + f' {str(self.age)} Let'


class Woman(Human):
    def __init__(self, v_name = 'Masha'):
        super().__init__(v_name)
        self.sex = 0



#obj1_petya.see_info()
#obj1_petya = Human('Petya')


#o_vasya = Human('Vasya')
#o_vasya.see_info()
#o_vasya.mobilize()
#o_vasya.see_info()

#print(o_vasya)


obj1_masha = Woman('Masha')
obj1_masha.see_info()
print(obj1_masha)