# Uporabnik naj vpiše začetno število
# Uporabnik naj vpiše končno število
# Izpiši fizbuzz za števila med začetnim in končnim (lahko tudi padajoče)
# 1, 2, Fizz, .... , 11
# 22, fizz, buzz, ...., 14

# Najprej preberite samo začetek in konec in izpišite samo st (brez fizzbuzz)

zacetno = int(input("Vpiši začetek:"))
konec = int(input("Vpiši konec:"))

# Nastavimo si smer, ki jo bomo potrebovali v range
if zacetno < konec: # ce je zacetno == konec je itak vseeno kaksna je smer
    smer = 1
else:
    smer = -1

for stevilo in range(zacetno, konec + smer, smer):
    if stevilo % 3 == 0 and stevilo % 5 != 0:
        print("Fizz")
    elif stevilo % 5 == 0 and stevilo % 3 != 0:
        print("Buzz")
    elif stevilo % 3 == 0 and stevilo % 5 == 0:
        print("Fizz Buzz")
    else:
        print(stevilo)