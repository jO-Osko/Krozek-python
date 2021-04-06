# Napišemo funkcijo za fakulteto

def izracunaj_fakulteto(stevilo):
    # Tako kot pri for zanki vse pišeš en nivo zamaknjeno
    # Ko poženeš in ugotoviš, zakaj je vrstni red printov 
    # tak kot je jih zakomentiraj 
    print("Računam fakulteto števila", stevilo)

    zmnozek_fakultete = 1

    for j in range(1, stevilo + 1):
        zmnozek_fakultete *= j

    print("Nehal sem računati fakulteto", stevilo)

    return zmnozek_fakultete


f_5 = izracunaj_fakulteto(5)

f_10 = izracunaj_fakulteto(10)

print(f_5, f_10)

