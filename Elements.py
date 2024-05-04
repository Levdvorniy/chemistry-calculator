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

def get_periodic_table():

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
    titanium = Element(22, "Titanium", "Titanium", "Ti", [2, 3, 4], [ElementsType.METAL], 4, 4, 4)
    Elements.append(titanium)
    vanadium = Element(23, "Vanadium", "Vanadium", "V", [2, 3, 4, 5], [ElementsType.METAL], 4, 4, 5)
    Elements.append(vanadium)
    chromium = Element(24, "Chromium", "Chromium", "Cr", [2, 3, 6], [ElementsType.METAL], 4, 4, 6)
    Elements.append(chromium)
    manganese = Element(25, "Manganese", "Manganum", "Mn", [2, 4, 7], [ElementsType.METAL], 4, 4, 7)
    Elements.append(manganese)
    iron = Element(26, "Iron", "Ferrum", "Fe", [2, 3], [ElementsType.METAL], 4, 4, 8)
    Elements.append(iron)
    cobalt = Element(27, "Cobalt", "Cobaltum", "Co", [2, 3], [ElementsType.METAL], 4, 4, 8)
    Elements.append(cobalt)
    nickel = Element(28, "Nickel", "Nickelum", "Ni", [2, 3], [ElementsType.METAL], 4, 4, 8)
    Elements.append(nickel)
    copper = Element(29, "Copper", "Cuprum", "Cu", [1, 2], [ElementsType.METAL], 4, 5, 1)
    Elements.append(copper)
    zinc = Element(30, "Zinc", "Zincum", "Zn", [2], [ElementsType.METAL], 4, 5, 2)
    Elements.append(zinc)
    gallium = Element(31, "Gallium", "Gallium", "Ga", [3], [ElementsType.METAL], 4, 5, 3)
    Elements.append(gallium)
    germanium = Element(32, "Germanium", "Germanium", "Ge", [2, 4], [ElementsType.METAL], 4, 5, 4)
    Elements.append(germanium)
    arsenic = Element(33, "Arsenic", "Arsenicum", "As", [3, 5], [ElementsType.NONMETAL], 4, 5, 5)
    Elements.append(arsenic)
    selenium = Element(34, "Selenium", "Selenium", "Se", [2, 4, 6], [ElementsType.NONMETAL], 4, 5, 6)
    Elements.append(selenium)
    bromine = Element(35, "Bromine", "Bromum", "Br", [1, 3, 5], [ElementsType.NONMETAL], 4, 5, 7)
    Elements.append(bromine)
    krypton = Element(36, "Krypton", "Krypton", "Kr", [0], [ElementsType.NONMETAL], 4, 5, 8)
    Elements.append(krypton)
    rubidium = Element(37, "Rubidium", "Rubidium", "Rb", [1], [ElementsType.METAL], 5, 6, 1)
    Elements.append(rubidium)
    strontium = Element(38, "Strontium", "Strontium", "Sr", [2], [ElementsType.METAL], 5, 6, 2)
    Elements.append(strontium)
    yttrium = Element(39, "Yttrium", "Yttrium", "Y", [3], [ElementsType.METAL], 5, 6, 3)
    Elements.append(yttrium)
    zirconium = Element(40, "Zirconium", "Zirconium", "Zr", [4], [ElementsType.METAL], 5, 6, 4)
    Elements.append(zirconium)
    niobium = Element(41, "Niobium", "Niobium", "Nb", [3, 5], [ElementsType.METAL], 5, 6, 5)
    Elements.append(niobium)
    molybdenum = Element(42, "Molybdenum", "Molybdenum", "Mo", [2, 3, 4, 5, 6], [ElementsType.METAL], 5, 6, 6)
    Elements.append(molybdenum)
    technetium = Element(43, "Technetium", "Technetium", "Tc", [4, 7], [ElementsType.METAL], 5, 6, 7)
    Elements.append(technetium)
    ruthenium = Element(44, "Ruthenium", "Ruthenium", "Ru", [2, 3, 4, 6, 8], [ElementsType.METAL], 5, 6, 8)
    Elements.append(ruthenium)
    rhodium = Element(45, "Rhodium", "Rhodium", "Rh", [2, 3, 4], [ElementsType.METAL], 5, 6, 8)
    Elements.append(rhodium)
    palladium = Element(46, "Palladium", "Palladium", "Pd", [2, 4], [ElementsType.METAL], 5, 6, 8)
    Elements.append(palladium)
    silver = Element(47, "Silver", "Argentum", "Ag", [1], [ElementsType.METAL], 5, 7, 1)
    Elements.append(silver)
    cadmium = Element(48, "Cadmium", "Cadmium", "Cd", [2], [ElementsType.METAL], 5, 7, 2)
    Elements.append(cadmium)
    indium = Element(49, "Indium", "Indium", "In", [3], [ElementsType.METAL], 5, 7, 3)
    Elements.append(indium)
    tin = Element(50, "Tin", "Stannum", "Sn", [2, 4], [ElementsType.METAL], 5, 7, 4)
    Elements.append(tin)
    antimony = Element(51, "Antimony", "Stibium", "Sb", [3, 5], [ElementsType.METAL], 5, 7, 5)
    Elements.append(antimony)
    tellurium = Element(52, "Tellurium", "Tellurium", "Te", [2, 4, 6], [ElementsType.METAL], 5, 7, 6)
    Elements.append(tellurium)
    iodine = Element(53, "Iodine", "Iodium", "I", [1, 3, 5, 7], [ElementsType.NONMETAL], 5, 7, 7)
    Elements.append(iodine)
    xenon = Element(54, "Xenon", "Xenon", "Xe", [0], [ElementsType.NONMETAL], 5, 7, 8)
    Elements.append(xenon)
    cesium = Element(55, "Cesium", "Caesium", "Cs", [1], [ElementsType.METAL], 6, 8, 1)
    Elements.append(cesium)
    barium = Element(56, "Barium", "Barium", "Ba", [2], [ElementsType.METAL], 6, 8, 2)
    Elements.append(barium)
    
    lantan = Element(57, "lantan", "lantan", "La", [0], [ElementsType.METAL], 6, 8, 3)
    
    hafnium = Element(72, "Hafnium", "Hafnium", "Hf", [4], [ElementsType.METAL], 6, 8, 4)
    Elements.append(hafnium)
    tantalum = Element(73, "Tantalum", "Tantalum", "Ta", [5], [ElementsType.METAL], 6, 8, 5)
    Elements.append(tantalum)
    tungsten = Element(74, "Tungsten", "Wolframium", "W", [2, 3, 4, 5, 6], [ElementsType.METAL], 6, 8, 6)
    Elements.append(tungsten)
    rhenium = Element(75, "Rhenium", "Rhenium", "Re", [4, 6, 7], [ElementsType.METAL], 6, 8, 7)
    Elements.append(rhenium)
    osmium = Element(76, "Osmium", "Osmium", "Os", [2, 3, 4, 6, 8], [ElementsType.METAL], 6, 8, 8)
    Elements.append(osmium)
    iridium = Element(77, "Iridium", "Iridium", "Ir", [2, 3, 4, 6], [ElementsType.METAL], 6, 8, 8)
    Elements.append(iridium)
    platinum = Element(78, "Platinum", "Platinum", "Pt", [2, 4], [ElementsType.METAL], 6, 8, 8)
    Elements.append(platinum)
    gold = Element(79, "Gold", "Aurum", "Au", [1, 3], [ElementsType.METAL], 6, 9, 1)
    Elements.append(gold)
    mercury = Element(80, "Mercury", "Hydrargyrum", "Hg", [1, 2], [ElementsType.METAL], 6, 9, 2)
    Elements.append(mercury)
    thallium = Element(81, "Thallium", "Thallium", "Tl", [1, 3], [ElementsType.METAL], 6, 9, 3)
    Elements.append(thallium)
    lead = Element(82, "Lead", "Plumbum", "Pb", [2, 4], [ElementsType.METAL], 6, 9, 4)
    Elements.append(lead)
    bismuth = Element(83, "Bismuth", "Bismuthum", "Bi", [3, 5], [ElementsType.METAL], 6, 9, 5)
    Elements.append(bismuth)
    polonium = Element(84, "Polonium", "Polonium", "Po", [2, 4], [ElementsType.METAL], 6, 9, 6)
    Elements.append(polonium)
    astatine = Element(85, "Astatine", "Astatine", "At", [1, 3, 5], [ElementsType.NONMETAL], 6, 9, 7)
    Elements.append(astatine)
    radon = Element(86, "Radon", "Radon", "Rn", [0], [ElementsType.NONMETAL], 6, 9, 8)
    Elements.append(radon)
    francium = Element(87, "Francium", "Francium", "Fr", [1], [ElementsType.METAL], 7, 10, 1)
    Elements.append(francium)
    radium = Element(88, "Radium", "Radium", "Ra", [2], [ElementsType.METAL], 7, 10, 2)
    Elements.append(radium)
    
    rutherfordium = Element(104, "Rutherfordium", "Rutherfordium", "Rf", [4], [ElementsType.METAL], 7, 10, 4)
    Elements.append(rutherfordium)
    dubnium = Element(105, "Dubnium", "Dubnium", "Db", [5], [ElementsType.METAL], 7, 10, 5)
    Elements.append(dubnium)
    seaborgium = Element(106, "Seaborgium", "Seaborgium", "Sg", [6], [ElementsType.METAL], 7, 10, 6)
    Elements.append(seaborgium)
    bohrium = Element(107, "Bohrium", "Bohrium", "Bh", [7], [ElementsType.METAL], 7, 10, 7)
    Elements.append(bohrium)
    hassium = Element(108, "Hassium", "Hassium", "Hs", [8], [ElementsType.METAL], 7, 10, 8)
    Elements.append(hassium)
    meitnerium = Element(109, "Meitnerium", "Meitnerium", "Mt", [0], [ElementsType.METAL], 7, 10, 8)
    Elements.append(meitnerium)
    darmstadtium = Element(110, "Darmstadtium", "Darmstadtium", "Ds", [0], [ElementsType.METAL], 7, 10, 8)
    Elements.append(darmstadtium)

    return Elements

lst = get_periodic_table()

for i in lst:
    if ElementsType.METAL in i.ElementTypes:
        print(i.designation)