moj_slovar = {
    1: "Miha",
    2: "Luka", 
    3: "Anja",
    4: "Mateja",
    17: "Katarina"
}

moj_slovar[4] = "Francka"

print(moj_slovar[17])
print(moj_slovar[4])

moj_slovar[-3] = "Janez"

print(moj_slovar[-3])

print(14 in moj_slovar)

print(17 in moj_slovar)

#### V while zanki uporabnika sprašujte po šifri in imenu izdelka
## To si shranjujte v nek slovar
# To počnite dokler ni šifra negativna
# Ko je negativna nehajte in izpišite cel slovar

print(moj_slovar)


for k in moj_slovar:
    print(k, moj_slovar[k])