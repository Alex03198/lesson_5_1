class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        for i in range(new_floor):
            j = i + 1
            if new_floor < self.number_of_floors:
                print(j)

h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик в деревне', 17)
h1.go_to(22)
h2.go_to(21)