slovar = {}

sifra = 100
while sifra > 0:
    break
    sifra = int(input("Vnesi šifro"))
    ime = input("Vnesi izdelek")
    slovar[sifra] = ime


print(slovar)

mnozica = { # set
    1, 4, 6, 89, 100
}

mnozica.add(1)
mnozica.remove(1)

stevilo_imen = {
    "janezek": 2
}

ze_poznano = {}
def janezek(index_kovanca):
    if index_kovanca in ze_poznano:
        return ze_poznano[index_kovanca]
    # dolg racun

    # dobis ven rezultat
    ze_poznano[index_kovanca] = rezultat

    return rezultat

    

# To predstavlja mojo zalogo:
trgovina = {
    "mleko": 10,
    "jajca": 15,
    "kruh":  7,
    "zeljenjava": 5
}

# Teče v while zanki in naredi sledeče:
# Izpiše kaj je na voljo v trgovini
# izberi možnost kupi/dodaj/izhod
# potem vpiše izdelek n količino in ga kupi/doda
# 
