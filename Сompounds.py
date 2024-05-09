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
    EXCHANGE = 3 # обмена

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


def parse_formula(formula):
    def multiply_elements(elements, multiplier):
        return {element: count * multiplier for element, count in elements.items()}

    def parse_subformula(subformula):
        element_stack = []
        current_element = ''
        multiplier = ''
        subformula_count = defaultdict(int)

        for char in subformula:
            if char.isdigit():
                multiplier += char  # Collecting number
            elif char.isupper():
                if current_element:
                    # Save previous element and multiplier
                    subformula_count[current_element] += int(multiplier) if multiplier else 1
                current_element = char
                multiplier = ''
            elif char.islower():
                current_element += char
            elif char == '(' or char == ')':
                pass  # Ignore as we assume no nested formulas here

        # Last element
        if current_element:
            subformula_count[current_element] += int(multiplier) if multiplier else 1

        return subformula_count

    # Splitting the formula into parts by '+' and process each part separately
    parts = formula.split('+')
    overall_count = defaultdict(int)

    for part in parts:
        # Extracting leading multipliers and the subformula
        match = re.match(r"(\d+)?([A-Za-z0-9()]+)(\d+)?", part.strip())
        if match:
            part_multiplier = int(match.group(1)) if match.group(1) else 1
            subformula = match.group(2)

            # Parsing the subformula
            subformula_elements = parse_subformula(subformula)

            # If we have a leading multiplier, apply it to all elements found
            if part_multiplier != 1:
                subformula_elements = multiply_elements(subformula_elements, part_multiplier)

            # Add/subtract to the overall count
            for element, count in subformula_elements.items():
                overall_count[element] += count

    return list(overall_count.items())

# Testing the function
formula = input()
result = parse_formula(formula)
print(result)
