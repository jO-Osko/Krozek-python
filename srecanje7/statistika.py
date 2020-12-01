input_file = open("podatki_v_letih.txt", "r")

imena = []
starosti = []

for line in input_file:
    podatki = line.split(",")

    imena.append(podatki[0])
    starosti.append(float(podatki[1]))

input_file.close()

# Najdimo minimum
# Iščemo po seznamu starosti
trenutni_min = starosti[0]
index_najmljajsega = 0

for i in range(0, len(starosti)):
    if starosti[i] < trenutni_min:
        trenutni_min = starosti[i]
        index_najmljajsega = i

print("Najmlajsi je star:", trenutni_min, "let.")
print("Najmlajsemu je ime:", imena[index_najmljajsega])

#### Izpisi najstarejšega in njegovo starost

trenutni_max = starosti[0]
index_najstarejsega = 0

for i in range(0, len(starosti)):
    if starosti[i] > trenutni_max:
        trenutni_max = starosti[i]
        index_najstarejsega = i

print("Najstarejši je star:", trenutni_max, "let.")
print("Ime mu je:", imena[index_najstarejsega])

#### Vsota

vsota = 0

for st in starosti:
    vsota += st

print("Skupaj so stari:", vsota)
povprecje = vsota / len(starosti)
print("Povprečno so stari:", povprecje)

### Izpiši vse, ki so starejši od povprečja (vsak v svojo vrstico)
print("Starejši od povprečja so")

indexi_starejsih = []

for i in range(len(starosti)):
    starost_trenutnega = starosti[i]
    if starost_trenutnega > povprecje:
        indexi_starejsih.append(i)
        print(imena[i])

#  0  1  2  3
# [0, 1, 3, 5] : indexi_starejsih
for index_starejsega in indexi_starejsih:
    print(imena[index_starejsega])

for i in range(len(indexi_starejsih)):
    print(
        imena[indexi_starejsih[i]]
    )




### Izpiši vse, ki so mlajši (ali enako stari) od povprečja, vsak v svojo vrstico
print("Mlajši od povprečja so")

#### Izpiši drugega najmlajšega/najstarejšega





