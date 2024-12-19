# "Магические здания"

class  House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor:
            for i in range(1, int(new_floor+1)):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)
h1.go_to(5)
print(h2.name, h2.number_of_floors)
h2.go_to(10)
print(h1)
print(h2)
print(len(h1))
print(len(h2))