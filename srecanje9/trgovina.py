
# DDV na hrano je 9.5%
# DDV na pijačo je 22%

class Produkt:
    # Cena mora biti na enoto kolicine
    # masa je tudi na enooto količine
    def __init__(self, cena, kolicina, ime, masa, je_hrana): 
        self.cena = cena
        self.kolicina = kolicina # Koliko imam zabojev jabolk
        self.ime = ime
        self.masa = masa
        self.je_hrana = je_hrana

    # Skupna masa točno enega produkta, ki je shranjen v self
    def skupna_masa(self):
        return self.masa * self.kolicina

    def izracunaj_stopnjo_davka(self):
        if self.je_hrana:
            return 0.095
        else:
            return 0.22
# Naredi dve funkciji: vrednost enega izdelka
# skupna vrednost zaloge 
    def skupna_vrednost(self):
        return self.kolicina * self.cena * (1 + self.izrazunaj_stopnjo_davka())

class Trgovina:
    def __init__(self, zaloga):
        # [
        #   (sifra1, produkt1),
        #   (sifra2, produkt2),
        # ]
        # [jabolko, hruske, riz, mleko, sok] -> 
        # prava_zaloga = [(1, jabolko), (2, hruske), ...] # 
        zacetna_sifra = 0
        
        zaloga_trgovine = [] # Sem notri dajemo (sifra, produkt)
        for pr in zaloga:
            zaloga_trgovine.append( [zacetna_sifra, pr])
            zacetna_sifra += 1

        self.zaloga = zaloga_trgovine

    

# Jabolka so v zabuju po 5 kg
# Zaboj stane 1.2 Eur
# Na voljo imamo 12 zabojev
jabolko = Produkt(1.2, 12, "Jabolka", 5.0, True)
hruske = Produkt(3.4, 10, "Hruške", 2.0, True)
riz = Produkt(0.5, 17, "Riž", 1.0, True)
mleko = Produkt(0.8, 100, "Mleko", 1.0, False)
sok = Produkt(1.8, 43, "Sok", 1.5, False)
# Naredi še 6 produktov, daj jih v seznam
# Napiši funkcijo, ki sprejme ta seznam in vrne skupno težo celotne trgovine

print(riz.skupna_masa())

trgovina = [jabolko, hruske, riz, mleko, sok]

trgovina_objekt = Trgovina(trgovina) # seznam izdelkov


# Popravi spodnjo funkcijo da uporablja metodo skupna_masa
# Posodbi izdelek, tako da dobi informacijo ali je hrana ali pijaca
# in si to nekako shrani
# Dodaj v svojo trgovino vsaj dve pijaci in hrani
# Dodaj metodo na izdelek, ki izracuna njegovo skupno vrednost

def skupna_teza_trgovine(seznam_izdelkov):
    skupna = 0
    for el in seznam_izdelkov:
        skupna += el.masa * el.kolicina
    
    return skupna

# prva naj vrne vrednost cele trgovine
# Drgua naj vrne skupno pštevilo izdelkov
# Tretja naj vrne izdelek z najvišjo vrednostjo
# 

print(skupna_teza_trgovine(trgovina))



