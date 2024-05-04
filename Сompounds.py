from enum import Enum

class Compounds(Enum):
    ALKALI = 1
    ACID = 2
    OXIDE = 3
    SALT = 4


print("Введите уравнение ОВР")
equation = input()

component1, component2 = equation.split(" + ")

print(component1)
print(component2)
