# Preberemo input
# Splitamo po vrsticah
# Gremo vrstico po vrstico

# ! Izvedi naslednji ukaz

# Stroj mora vedeti:
#    - vrednost -> OK
#    - v kateri vrstici je -> OK
#    - vse vrstice, ki jih je ze izvedel
#    - Seznam ukazov -> OK

class Ukaz:
    def __init__(self, tip_ukaza, stevilka):
        self.tip_ukaza = tip_ukaza
        self.stevilka = stevilka

class Machine:
    def __init__(self, ukazi):
        self.ukazi = ukazi
        self.akumulator = 0 # To je tisto kar se spreminja
        self.line = 0 # Index ukaza na katerem smo

    def naredi_korak(self):
        pass


    def pozeni_do_konca(self):
        # Naj vrne: Ali se zacikla, ali pa se izvede do konca

        pass

ukazi = [
    # Ukaz("nop", 0),
    # Ukaz("acc", 1),
]

for ukaz in ukazi:
    if hocemo_zamenjati(ukaz):
        zamenjani = ukazi.zamenjaj(ukaz)
        stroj = Machine(zamenjani)
        stroj.pozeni_do_konca()

# Preberemo ukaze
# za vsako vrstico, splitaš po presledku, 
# dam v ukaz, potem pa ta ukaz dodam v seznam ukazov



a = [1, 5, -3, 5, 6, 19]

a.sort(reverse=True)
print(a)