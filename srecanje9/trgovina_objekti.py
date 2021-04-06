
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
        self.roba_v_skladiscu = zaloga_trgovine
    
    def stevilo_razlicnih_izdelkov(self):
        stevilo = 0
        for izdelek in self.zaloga:
            # izdelek = [sifra, produkt]
            pr = izdelek[1] # to je tipa Produkt
            # pr ima cel kup stvari (glej class Produkt)
            if pr.kolicina > 0:
                stevilo += 1

        return stevilo


# nekaj novega |-> Dodaj funkcijo kupi(self, id_izdelka, sprememba_kolicine)
# nekaj novega |-> Funkcija naj se sprehodi po zalogi (self.zaloga)
# nekaj novega |-> najde izdelek s pravi id-jem in popravi njegovo zalogo
# nekaj novega |-> Naj vrne True, ko ga najde in uspesno popravi zalogo

# Popravljanje zaloge:  pr.kolicina -= sprememba_kolicine
# While zanka: uporabniku naj izpiše id-je izdelkov v trgovini, 
# Ga vpraša za id in količino
# in nakupi ta izdelek
# Dokler ne vpiše id-ja 0


# Popravi spodnjo funkcijo da uporablja metodo skupna_masa
# Posodbi izdelek, tako da dobi informacijo ali je hrana ali pijaca
# in si to nekako shrani
# Dodaj v svojo trgovino vsaj dve pijaci in hrani
# Dodaj metodo na izdelek, ki izracuna njegovo skupno vrednost

def skupna_teza_trgovine_celotne_trgovine(seznam_izdelkov):
    skupna = 0
    for el in seznam_izdelkov:
        skupna += el.masa * el.kolicina
    
    return skupna

# prva naj vrne vrednost cele trgovine
# Drgua naj vrne skupno pštevilo izdelkov
# Tretja naj vrne izdelek z najvišjo vrednostjo
# celotna masa trgovine
# vrne maso hrane
# vrne maso pijače 

#print(skupna_teza_trgovine_celotne_trgovine(trgovina))


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
prazna = Trgovina([])

trgovina = [jabolko, hruske, riz, mleko, sok]

trgovina_objekt = Trgovina(trgovina) # seznam izdelkov
print(trgovina_objekt.stevilo_razlicnih_izdelkov())

print(prazna.stevilo_razlicnih_izdelkov())







class Task:
    def __init__(self, label, type, command):
        pass