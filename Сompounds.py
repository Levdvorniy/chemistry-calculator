from enum import Enum
import re
from Elements import get_periodic_table, ElementsType

PERIODIC_TABLE = get_periodic_table()

class Compounds(Enum): # химические соединения
    ALKALI = 1 # основания
    ACID = 2 # кислоты
    OXIDE = 3 # оксиды
    SALT = 4 # соли

    def __str__(self):
        return self.name

class Redox(Enum): # реакции
    CONNECTION = 1 # соединения
    DECOMPOSITION = 2 # разложения
    SUBSTRITUTION = 3 # замещения
    EXCHANGE = 3 # обмена

class Catalisator(Enum):
    ELECTRISITY = 1
    PLATINUM = 2
    TEMPERATURE = 3

def determine_type_of_compounds(component):

    galogens = [i for i in PERIODIC_TABLE if ElementsType.GALOGEN in i.ElementTypes]
    # print([i.designation for i in galogens])

    if any(i.designation in component for i in galogens):
        return Compounds.SALT
    if "OH" in component:
        return Compounds.ALKALI
    if "O" in component:
        return Compounds.OXIDE
    else:
        return Compounds.ACID

# def get_catalisator():


def determine_type_of_reactions(types_of_components):

    if len(types_of_components) == 1:
        return Redox.DECOMPOSITION
    if Compounds.ALKALI in types_of_components and Compounds.SALT in types_of_components:
        return Redox.CONNECTION
    else:
        return Redox.SUBSTRITUTION

def compute_coeffs_for_equations(compounds):
    components = []
    coeffs = []
    result = list(zip(components, coeffs))

    return result

print("Введите уравнение ОВР в формате A + B + ...:")
equation = input()

components = equation.split(" + ")
result = [determine_type_of_compounds(i) for i in components]
res = zip(components, result)

print(list(res))
