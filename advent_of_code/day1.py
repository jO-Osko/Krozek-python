# Naredimo program, ki prebere številke iz datoteke
# izpiše naj vse pare kjer je razilka večja kot 200

import os.path
import time


stevilke = []

input_file = open(os.path.join("advent_of_code", "day1.in"), "r")

for line in input_file:
    stevilke.append(int(line))

print(len(stevilke))

# stevilke = [-1, 4, 13, -10, 1, 3]
# Možnost 1


# Tukaj so stevilke posortirane
zacetek = time.time()
for index_prva in range(0, len(stevilke)):
    # Dobimo ven prvo
    prva_stevilka = stevilke[index_prva]

    # Gremo po vseh stevilkah, ki so kasneje v seznamu
    for index_druga in range(index_prva + 1, len(stevilke)):
        druga_stevilka = stevilke[index_druga]

        if prva_stevilka + druga_stevilka == 2020:
            print(prva_stevilka * druga_stevilka)
            break
# alt +  shift + puščica dol
        # Popravi tako, da 
konec = time.time()

print("Trajanje: ", konec - zacetek)

# Ideja, hkrati gledam na dve številki in prilagajam katero popravim

levi_i = 0
desni_i = len(stevilke) - 1

zacetek = time.time() # vrne ševilo sekund od 1.1.1970

iskana_vsota = 2020
stevilke.sort()

# Dokler se ne zamenjata
while levi_i <= desni_i:
    vsota = stevilke[levi_i] + stevilke[desni_i]
    # Rabim večjo vsoto
    if vsota < iskana_vsota:
        levi_i += 1
    # Rabim manjšo vsoto
    elif vsota > iskana_vsota:
        desni_i -= 1
    else:
        print(stevilke[levi_i] * stevilke[desni_i])
        break

konec = time.time()
print("Trajanje: ", konec-zacetek)


