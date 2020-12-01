# Uporabnik vpise zacetno in koncno stevilo
# Morate izpisat
# [zacetno_stevilo, 1, 2, bum, 4, 5, bum, 7, 8, bum, ..., koncno_stevilo ]
# Korak 2:
# Uporabnik izpise katero stevilo je pogoj za bum: 17
# bum=3
# stejem po 2
# Korak 3:
# [1, bum, 5, 7, bum, ...]

# Stejem po 4, bum = 5
# [1, 5, 9, 13]
# [1, bum, 9, 13...]

zacetek = int(input("vnesi zacetek"))
konec = int(input("vnesi konec"))
bum = int(input("vnesi bum"))
korak = int(input("vnesi korak"))

if zacetek < konec:
    smer = 1
else:
    smer = -1

for st in range(zacetek, konec + smer, korak*smer):
    if st%bum == 0:
        print("bum")
    else:
        print(st)