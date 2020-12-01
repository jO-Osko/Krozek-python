# Collatzevo zaporedje
# Ce je stevilo deljivo z 2, potem ga delim z 2
# Ce ni deljivo z 2, potem ga množim s 3 in prištejem 1
# x -> x // 2 (Če je deljiv z 2)
# x -> 3*x + 1 (Če ni deljiv z 2)
# Končam, ko je x == 1
# 100 -> 50 -> 25 -> 76 -> 38 -> 19 -> ....... -> 1
# Uporabnik naj vpiše številko, progam pa izpiše vse člene od številke do 1


stevilo = int(int(input("Vnesi začetek")))

# To bomo potrebovali na koncu za izpis
zacetno_stevilo = stevilo
stevilo_korakov = 0

while stevilo != 1:
    # Ponavljaj postopek
    # a % b nam da ostanek pri deljenju a z b
    print(stevilo)
    stevilo_korakov += 1

    if stevilo % 2 == 0:
        stevilo = stevilo // 2
    else:
        stevilo = stevilo * 3 + 1

print(stevilo)
print("Zaporedje, ki se zacne z", zacetno_stevilo, "ima", stevilo_korakov, "korakov.")

