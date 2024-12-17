class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
                for i in range(1, new_floor + 1):
                    if 1 <= new_floor <= self.number_of_floors:
                        print(i)
                    else:
                        print('Такого этажа не существует')
                        break
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return



h1 = House('ЖК Парус', 15)
h2 = House('ЖК EboLand', 69)
h1.go_to(4)
h2.go_to(70)

print(h1 == h2) #__eq__
print(h1 < h2) #__it__
print(h2 <= h1) #__le__
print(h2 > h1) #__gt__
print(h2 >= h1) #__ge__
print(h1 != h2) #__ne__

h1 = h1 + 2 # __add__
print(h1)
print(h1 == h2)

h1 += 2 # __iadd__
print(h1)

h2 = 2 + h2 # __radd__
print(h2)

