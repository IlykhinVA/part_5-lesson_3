class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return 'Название: ' + self.name + ', количество этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):
        self.number_of_floors = other.number_of_floors + other
        return self.number_of_floors

    def __iadd__(self, other):
        self.number_of_floors += other
        return self.number_of_floors

    def __radd__(self, other):
        new_height = other + self.number_of_floors
        return new_height

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


first_house = House('ЖК "Эльбрус"', 10)
second_house = House('ЖК "Акация"', 20)

print(first_house)
print(second_house)
print(first_house == second_house)
first_house.number_of_floors = first_house.number_of_floors + 10
print(first_house)
print(first_house == second_house)
first_house.number_of_floors += 10
print(first_house)
second_house.number_of_floors = 10 + second_house.number_of_floors
print(second_house)
print(first_house > second_house)
print(first_house >= second_house)
print(first_house < second_house)
print(first_house <= second_house)
print(first_house != second_house)
