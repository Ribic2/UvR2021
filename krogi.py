import math as m
# Hvala, Miklavž, čeprav bi tole znali napisati tudi sami.
# Obljubimo, da se jo bomo potrudili razumeti
# v
def ocisti_slovar(d):
    return {k: v for k, v in d.items() if v}


# U, tale je pa kar zaresna. V ponedeljek bomo prosili profesorja,
# da nam jo razloži, ker smo radovedni kako deluje.
# v
def notranjost(krogi):
    return set().union(*map(set, vsebovanost(krogi).values()))

# Eh, to bi pa res znali sami. Bomo še ostale naredili podobno.
def ptici(krogi):
    return ptici0(vsebovanost(krogi), notranjost(krogi))

def polmeri(krogi):
    return {i[2] for i in krogi}

def veliki(r0, krogi):
    return {(krog[0],krog[1]) for krog in krogi if krog[2] >= r0}

def obsegi(krogi):
    return sum(2 * pi * polmer for x, y, polmer in krogi)

def najlevo(krogi):
    return min([x - polmer for x, y, polmer in krogi])

def povrsina(krogi):
    return (max([x+polmer for x, y, polmer in krogi]) - min([x-polmer for x, y, polmer in krogi])) * (max([y+polmer for x, y, polmer in krogi]) - min([y-polmer for x, y, polmer in krogi]))

#def ocisti_slovar(d):

def znotraj(x0, y0, r0, krogi):
    return [krog for krog in krogi if m.sqrt(pow((x0 - krog[0]), 2) + pow((y0 - krog[1]), 2)) < r0 and krog[2
] < r0]

def vsebovanost(krogi):
    return {(x0, y0, r0):znotraj(x0, y0, r0, krogi) for x0, y0, r0 in krogi if len(znotraj(x0, y0, r0, krogi)) > 0 }

def ptici0(vsebovani, notranji):
    return {(x, y) for x, y, r in vsebovani if len(vsebovani[x, y, r]) == 2 and (x, y, r) not in notranji and len(znotraj(vsebovani[x, y, r][0][0], vsebovani[x, y, r][0][1], vsebovani[x, y, r][0][2], krogi)) == 0}



krogi = [
    (164.4, 136.8, 50.8),
    (59.2, 182.8, 50.8),
    (282.8, 71.5, 45.6),
    (391, 229.4, 58.4),
    (259.9, 186, 47.6),
    (428, 89, 63.2),
    (88.6, 44.3, 37.5),
    (371.6, 233.6, 10.6),
    (408.7, 210.5, 8.9),
    (398.1, 95.5, 13),
    (449.5, 99.6, 13.6),
    (455.4, 66.5, 12.4),
    (139.6, 138, 10.6),
    (185, 138, 10.6),
    (69.8, 46.5, 10.6),
    (267.4, 51.7, 17.2),
    (225.8, 187.3, 7.5),
    (242.8, 187.3, 7.5),
    (259.8, 187.3, 7.5),
    (276.7, 187.3, 7.5),
    (293.7, 187.3, 7.5),
    (267.4, 51.7, 10.6),
    (99.6, 43.1, 17.2),
    (99.6, 43.1, 10.6),
    (150.3, 245.5, 50.8),
    (144.3, 243.6, 38.8),
    (127.3, 245.5, 7.5),
    (161.3, 245.5, 7.5)]



import time
import ast
import unittest
from math import pi


print(vsebovanost(krogi).keys())
