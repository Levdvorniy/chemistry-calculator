from enum import Enum

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
        self.ElementType = ElementType
        self.period = period
        self.row = row
        self.group = group

    def __str__(self):
        return "Name = " + self.name + ",\n" + "Designation = " + self.designation + ",\n" + "Valences = " + str(self.valence) + ",\n" + "ElementType = " + str(self.ElementType[0])

Elements = []

Elements.append(Element(1, "Hydrogen", "Hydrogenium", "H", [-1, +1], [ElementsType.NONMETAL], 1, 1, 1))
Elements.append(Element(2, "Helium", "Helium" , "He", [-1, +1], [ElementsType.NONMETAL], 1, 1, 8))
Elements.append(Element(3, "Lithium", "Lithium" , "Li", [-1, +1], [ElementsType.METAL], 2, 2, 1))
Elements.append(Element(4, "Beryllium", "Beryllium" , "Be", [-1, +1], [ElementsType.NONMETAL], 2, 2, 2))
Elements.append(Element(5, "Boron", "Borum" , "He", [-1, +1], [ElementsType.NONMETAL], 2, 2, 3))
Elements.append(Element(6, "Carbon", "Carboneum" , "C", [-1, +1], [ElementsType.NONMETAL], 2, 2, 4))
Elements.append(Element(7, "Nitrogen", "Nitrogenium" , "N", [-1, +1], [ElementsType.NONMETAL], 2, 2, 5))
Elements.append(Element(8, "Oxygen", "Oxygenium" , "O", [-1, +1], [ElementsType.NONMETAL], 2, 2, 6))
Elements.append(Element(9, "Fluorine", "Fluorum" , "F", [-1, +1], [ElementsType.NONMETAL, ElementsType.GALOGEN], 2, 2, 7))
Elements.append(Element(10, "Neon", "Neon" , "Ne", [-1, +1], [ElementsType.NONMETAL], 2, 2, 8))
Elements.append(Element(11, "Sodium", "Natrium", "Na", [-1, +1], [ElementsType.METAL], 3, 3, 1))
Elements.append(Element(12, "Magnesium", "Magnesium" , "Mg", [-1, +1], [ElementsType.NONMETAL], 3, 3, 2))
Elements.append(Element(13, "Aluminium", "Aluminium" , "Al", [-1, +1], [ElementsType.METAL], 3, 3, 3))
Elements.append(Element(14, "Silicon", "Silicium" , "Si", [-1, +1], [ElementsType.NONMETAL], 3, 3, 4))
Elements.append(Element(15, "Phosphorus", "Phosphorus" , "P", [-1, +1], [ElementsType.NONMETAL], 3, 3, 5))
Elements.append(Element(16, "Sulfur", "Sulfur" , "S", [-1, +1], [ElementsType.NONMETAL], 3, 3, 6))
Elements.append(Element(17, "Chlorine", "Chlorum" , "Cl", [-1, +1], [ElementsType.NONMETAL], 3, 3, 7))
Elements.append(Element(18, "Argon", "Argon" , "Ar", [-1, +1], [ElementsType.NONMETAL], 3, 3, 8))
Elements.append(Element(19, "Potassium", "Kalium" , "K", [-1, +1], [ElementsType.METAL], 4, 4, 1))
Elements.append(Element(20, "Calcium", "Calcium" , "Ca", [-1, +1], [ElementsType.METAL], 4, 4, 2))
print(Elements[0])