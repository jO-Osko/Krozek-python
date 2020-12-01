# Stevilo z najdaljso verigo

konec = 10**4

najdaljsa_veriga = -1
stevilo_z_najdaljso_verigo = -1

for stevilo in range(1, konec):
    zacetno_stevilo = stevilo
    # za vsako stevilo bomo na novo pogledal kako dolga je veriga
    stevilo_korakov = 0
    while stevilo != 1:
        # Ponavljaj postopek
        # a % b nam da ostanek pri deljenju a z b
        stevilo_korakov += 1

        if stevilo % 2 == 0:
            stevilo = stevilo // 2
        else:
            stevilo = stevilo * 3 + 1
    # 17 + ":"

    # Trenutno število je najdaljše zaenkrat
    if najdaljsa_veriga < stevilo_korakov:
        najdaljsa_veriga = stevilo_korakov
        stevilo_z_najdaljso_verigo = zacetno_stevilo

    # print(str(zacetno_stevilo) + ": " + str(stevilo_korakov))

print("Najdaljso verigo ima", stevilo_z_najdaljso_verigo, "ki je dolga", najdaljsa_veriga)


