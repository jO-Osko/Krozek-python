sez = [1, 2, 4, 8, 9, -3]
print(len(sez))

print(sez[3], sez[0], )
print(sez[-1], sez[-4], sez[-len(sez)])

sez[3] = 200

for i in range(len(sez)):# 0, 1, 2, ..., 5
    print(i, sez[i], sez[i]**2)

a = []
a.append(17)
a.append(34)
print(a)
min
# Napiši funkcijo minimum, maximum, vsota, produkt
# Dobijo seznam in vrnejo 
# Funkcija fakulteta ki dobi seznam števil in vrne seznam fakultet števil
# [1, 5, 8, 3] -> [1!, 5!, 8!, 3!]
