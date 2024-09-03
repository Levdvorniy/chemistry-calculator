from enum import Enum
import re
from Elements import get_periodic_table, ElementsType
from collections import defaultdict

PERIODIC_TABLE = get_periodic_table()

class Compounds(Enum): # химические соединения
    ALKALI = 1 # основания
    ACID = 2 # кислоты
    OXIDE = 3 # оксиды
    SALT = 4 # соли

    # def __str__(self):
    #     return self.name

class Redox(Enum): # реакции
    CONNECTION = 1 # соединения
    DECOMPOSITION = 2 # разложения
    SUBSTRITUTION = 3 # замещения
    EXCHANGE = 4 # обмена

class Catalisator(Enum):
    ELECTRISITY = 1
    PLATINUM = 2
    TEMPERATURE = 3
    NOTHING = 4

def determine_type_of_compounds(component):

    metals = [i for i in PERIODIC_TABLE if ElementsType.METAL in i.ElementTypes]
    # print([i.designation for i in galogens])

    if any(i.designation in component for i in metals):
        return Compounds.SALT
    if any(i.designation in component for i in metals) and "OH" in component:
        return Compounds.ALKALI
    if "O" in component:
        return Compounds.OXIDE
    else:
        return Compounds.ACID

def get_catalisator():
    
    return Catalisator.NOTHING


# def parse_formula(formula):
#     components = formula.split(" + ")
#     elements = [list(filter(None, re.split(r"([A-Z][a-z]*\d*|\([A-Z0-9a-z0-9]+\)\d*)", component))) for component in components]

#     return elements

def parse_atoms(formula):
    components = formula.split(" + ")
    elements = [list(filter(None, re.findall(r"[A-Z][a-z]|[A-Z]|\d*", component))) for component in components]
    
    return elements

def get_count_of_atoms(formula):
    count_of_moleculs = 1
    result = {}
    for molecul in formula:
        if molecul[0].isdigit():
            count_of_moleculs = int(molecul[0])
        for i in range(len(molecul)-1):
            count_of_atoms = 1
            if molecul[i].isinstance() and molecul[i+1].isdigit() and molecul[i] not in result.keys():
                result[molecul[i]] = count_of_moleculs * int(molecul[i+1])
            if molecul[i].isinstance() and molecul[i+1].isdigit() and molecul[i] in result.keys():
                result[molecul[i]] += count_of_moleculs * int(molecul[i+1])
    return result

def get_result_of_redox(formula):

    components = formula.split(" + ")
    compounds = [determine_type_of_compounds(i) for i in components]
    result = parse_atoms(formula)
    if Compounds.ACID in compounds and Compounds.OXIDE in compounds:
        return components[compounds.index(Compounds.ALKALI)]
    return components[compounds.index(Compounds.ALKALI)]


# Testing the function
formula = input()
result = parse_atoms(formula)
# print(get_result_of_redox(formula))
print(result)

# print(parse_atoms("2Na23(O2H3)45"))