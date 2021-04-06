from functools import lru_cache

import sys
f = open("srecanje9/janezek.in")

nizi = f.readline().split(",")
stevilke = []
for c in nizi:
    stevilke.append(int(c))
print(stevilke)

zapomnjeno = {}



@lru_cache(maxsize=None)
def maksimum(mesto_janezka, dolzina_zadnjega_skoka=3): 
    if (mesto_janezka, dolzina_zadnjega_skoka) in zapomnjeno:
        return zapomnjeno[(mesto_janezka, dolzina_zadnjega_skoka)]

    if len(stevilke) - 1 == mesto_janezka:
        return stevilke[mesto_janezka]
    if mesto_janezka >= len(stevilke):
        return 0
    # Izberemo
    prva_moznost = stevilke[mesto_janezka] + \
        maksimum(mesto_janezka + 2)
    # Ne izberemo
    druga_moznost = maksimum(mesto_janezka + 1)

    rez = max(prva_moznost, druga_moznost)

    zapomnjeno[(mesto_janezka, dolzina_zadnjega_skoka)] = rez

    return rez


print(maksimum(0))

