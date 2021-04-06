class Uporabnik:
    def __init__(self, odgovori):
        self.odgovori = odgovori

class Skupina:
    def __init__(self, uporabniki):
        self.uporabniki = uporabniki

    def dolzina_razlicnih(self):
        print(len(self.uporabniki))

        do_sedaj = set()
        for uporabnik in self.uporabniki:
            # Odgovore enega uporabnika dam v množico
            mnozica_odg = set(uporabnik.odgovori)
            # In jo združim z ostalimi do sedaj
            do_sedaj = do_sedaj.union(mnozica_odg)
            # Tole bi lahko napisal tudi kot do_sedaj |= mnozica_odg

        return len(do_sedaj)

    def dolzina_enakih(self):
        print(len(self.uporabniki))

        do_sedaj = set(self.uporabniki[0].odgovori) 
        for uporabnik in self.uporabniki:
            # Odgovore enega uporabnika dam v množico
            mnozica_odg = set(uporabnik.odgovori)
            # In jo združim z ostalimi do sedaj
            do_sedaj = do_sedaj.intersection(mnozica_odg)
            # Tole bi lahko napisal tudi kot do_sedaj |= mnozica_odg

        return len(do_sedaj)

import os.path

if 3 > 2:
    pass

vhod = open(
    os.path.join("advent_of_code", "day6.in"), 
    "r").read()

skupine = []

skupine_vrstic = vhod.split("\n\n")
for skupina in skupine_vrstic: # Imamo eno skupino
    
    uporabniki = [] # Seznam uporabnikov
    besede_uporabnikov = skupina.split("\n")
    
    for beseda in besede_uporabnikov:
        uporabniki.append(Uporabnik(beseda))
    
    skupina = Skupina(uporabniki)
    skupine.append(skupina)

vsota = 0
vsota2 = 0
for skupina in skupine:
    # Python v ozadju poklice nekaj podobnega kot
    # dolzina_razlicnih(skupina) 
    vsota += skupina.dolzina_razlicnih() 
    vsota2 += skupina.dolzina_enakih() 

print("Končna vsota:", vsota, "Rezultat naloge2: ", vsota2)
