slovar = {
    1: "Ena", 2: "Dva", 200: "Dvesto", -300: "minus zelo veliko"
}

print(slovar[1])
print(slovar[-300])

slovar["petnajst"] = "pet + deset <- To je vrednost"
print(slovar)

for j in slovar:
    break
    print(j, slovar[j]) # Po ključih

for k, v in slovar.items(): # Po parih (kljuc, vrednost)
    break
    print(k, v) # v == slovar[k]


print(1 in slovar, 201 in slovar)

exit()
































slovar = {1: "Ena", 2: "Dva", 3: "Tri"}

neki = slovar[1] 
drugo = slovar[3]

slovar[15] = "Petnajst"
slovar[1] = "EEEEEEEEna"

print(neki, drugo)


print(slovar)

for k in slovar:
    print(k, slovar[k])

# 
for k, v in slovar.items():
    print(k, v)


print(3 in slovar, 99 in slovar)