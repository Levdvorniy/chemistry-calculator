from enum import Enum
import re
from Elements import get_periodic_table
class Compounds(Enum): # химические соединения
    ALKALI = 1 # основания
    ACID = 2 # кислоты
    OXIDE = 3 # оксиды
    SALT = 4 # соли

class Redox(Enum): # реакции
    CONNECTION = 1 # соединения
    DECOMPOSITION = 2 # разложения
    SUBSTRITUTION = 3 # замещения
    EXCHANGE = 3 # обмена

def determine_type_of_compounds(component):

    if "OH" in component:
        return Compounds.ALKALI
    if "O" in component:
        return Compounds.OXIDE
    else:
        return Compounds.ACID


def determine_type_of_reactions(type_of_components):

    if len(type_of_components == 1):
        return Redox.DECOMPOSITION

    type_of_reaction = Redox.CONNECTION
    
    return type_of_reaction


periodic_table = get_periodic_table()

print("Введите уравнение ОВР")
equation = input()

components = equation.split(" + ")
result = [determine_type_of_compounds(i) for i in components]
res = zip(components, result)

print(list(res))
