# Naredili bomo objekt User
# V tem objektu bomo shranili vse podatke o teh userju
# - ime, letnica_rojstva, priimek

class User:
    # Te stvari podamo ob kreiranju objekta uporabnik
    def __init__(self, ime, priimek, letnica_rojstva):
        self.ime = ime
        self.priimek = priimek
        self.letnica_rojstva = letnica_rojstva
        self.starost = 2020 - letnica_rojstva
        self.polno_ime = self.priimek + ", " + self.ime

    # Pokliče se, ko printamo objekt
    # Vrne naj lep niz, ki predstavlja uporabnika
    # recimo "Jaz sem ime, priimek, rojen: leto, star: stevilka"
    # parameter `self` je ravno tisti uporabnik o katerem govorimo
    def __str__(self):
        return "Jaz sem ime, priimek, rojen: leto, star: stevilka"

filip = User("Filip", "Koprivec", 1995)
arja = User("Arja Eva", "Hvala", 2006)
nejc = User("Nejc", "Petrič", 2005)
domen = User("Domen", "Korenini", 2004)
matija = User("Matija", "Ihan Švigelj", 2004)

vsi_uporabniki = [filip, arja, nejc, domen, matija]

# Izpiši polno ime najmlajsega v seznamu vsi_uporabniki

najmlajsi = vsi_uporabniki[0]
for u in vsi_uporabniki:
    if u.starost < najmlajsi.starost:
        najmlajsi = u

print("Najmlajši je:", najmlajsi.starost, najmlajsi)




