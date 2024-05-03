from enum import Enum
from typing import Any

class ElementsType(Enum):
    METAL = 1
    NONMETAL = 2
    GALOGEN = 3
    LANTHANIDE = 4

class Element:
    the_number_in_the_periodic_table = 0
    group = 0
    period = 0
    row = 0
    name = ""
    the_name_is_in_latin = ""
    designation = ""
    valences = []
    ElementTypes = []

    def __init__(self, the_number_in_the_periodic_table, name,  the_name_is_in_latin, designation, valence, ElementType, period, row, group):
        self.the_number_in_the_periodic_table = the_number_in_the_periodic_table
        self.name = name
        self.the_name_is_in_latin = the_name_is_in_latin
        self.designation = designation
        self.valence = valence
        self.ElementTypes = ElementType
        self.period = period
        self.row = row
        self.group = group

    def __str__(self):
        return "Name = " + self.name + ",\n" + "Designation = " + self.designation + ",\n" + "Valences = " + str(self.valence) + ",\n" + "ElementType = " + str(self.ElementType[0])

Elements = []

hydrogen0 = Element(1, "Hydrogen", "Hydrogenium", "H", [1], [ElementsType.NONMETAL], 1, 1, 1)
Elements.append(hydrogen0) 
hydrogen = Element(1, "Hydrogen", "Hydrogenium", "H", [1], [ElementsType.NONMETAL], 1, 1, 7)
Elements.append(hydrogen)
helium = Element(2, "Helium", "Helium" , "He", [0], [ElementsType.NONMETAL], 1, 1, 8)
Elements.append(helium)
lithium = Element(3, "Lithium", "Lithium" , "Li", [1], [ElementsType.METAL], 2, 2, 1)
Elements.append(lithium)
beryllium = Element(4, "Beryllium", "Beryllium" , "Be", [2], [ElementsType.NONMETAL], 2, 2, 2)
Elements.append(beryllium)
boron = Element(5, "Boron", "Borum" , "He", [3], [ElementsType.NONMETAL], 2, 2, 3)
Elements.append(boron)
carbon = Element(6, "Carbon", "Carboneum" , "C", [2, 4], [ElementsType.NONMETAL], 2, 2, 4)
Elements.append(carbon)
nitrogen = Element(7, "Nitrogen", "Nitrogenium" , "N", [1, 2, 3, 4], [ElementsType.NONMETAL], 2, 2, 5)
Elements.append(nitrogen)
oxygen = Element(8, "Oxygen", "Oxygenium" , "O", [2], [ElementsType.NONMETAL], 2, 2, 6)
Elements.append(oxygen)
fluorine = Element(9, "Fluorine", "Fluorum" , "F", [1], [ElementsType.NONMETAL, ElementsType.GALOGEN], 2, 2, 7)
Elements.append(fluorine)
neon = Element(10, "Neon", "Neon" , "Ne", [0], [ElementsType.NONMETAL], 2, 2, 8)
Elements.append(neon)
sodium = Element(11, "Sodium", "Natrium", "Na", [1], [ElementsType.METAL], 3, 3, 1)
Elements.append(sodium)
magnesium = Element(12, "Magnesium", "Magnesium" , "Mg", [2], [ElementsType.NONMETAL], 3, 3, 2)
Elements.append(magnesium)
aluminium = Element(13, "Aluminium", "Aluminium" , "Al", [3], [ElementsType.METAL], 3, 3, 3)
Elements.append(aluminium)
silicon = Element(14, "Silicon", "Silicium" , "Si", [2, 4], [ElementsType.NONMETAL], 3, 3, 4)
Elements.append(silicon)
phosphorus = Element(15, "Phosphorus", "Phosphorus" , "P", [3, 5], [ElementsType.NONMETAL], 3, 3, 5)
Elements.append(phosphorus)
sulfur = Element(16, "Sulfur", "Sulfur" , "S", [2, 4, 6], [ElementsType.NONMETAL], 3, 3, 6)
Elements.append(sulfur)
chlorine = Element(17, "Chlorine", "Chlorum" , "Cl", [1, 3, 5, 7], [ElementsType.NONMETAL, ElementsType.GALOGEN], 3, 3, 7)
Elements.append(chlorine)
argon = Element(18, "Argon", "Argon" , "Ar", [0], [ElementsType.NONMETAL], 3, 3, 8)
Elements.append(argon)
potassium = Element(19, "Potassium", "Kalium" , "K", [1], [ElementsType.METAL], 4, 4, 1)
Elements.append(potassium)
calcium = Element(20, "Calcium", "Calcium" , "Ca", [2], [ElementsType.METAL], 4, 4, 2)
Elements.append(calcium)
scandium = Element(21, "Scandium", "Scandium", "Sc", [3], [ElementsType.METAL], 4, 4, 3)
Elements.append(scandium)
titanium = Element(22, "Titanium", "Titanium", "Ti", [2, 3, 4], [ElementsType.METAL, 4, 4, 4])

for i in Elements:
    if ElementsType.METAL in i.ElementTypes:
        print(i.designation)