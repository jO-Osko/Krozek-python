# Preprosta trgovina

# Koliko različnih izdelkov si kupil

# Kaj si kupil
# koliko kosov
# Koliko stane en kos

# Skupaj si zapravil: ___ $

skupno_st_kosov = 0
skupna_cena = 0.0 # Necelo število

ponavljaj = True
while ponavljaj:
    # Vprašamo za posamezne
    ime = input("Kaj si kupil")
    st_kosov = int(input("Koliko kosov?"))

    if st_kosov == 0:
        print("Končal si z nakupovanjem")
        ponavljaj = False
        break
    cena = float(input("Koliko stane en?"))

    skupno_st_kosov += st_kosov
    skupna_cena += cena

print("Skupaj si zapravil:" + str(skupna_cena) + "$")
print("Skupaj si nakupil:" + str(skupno_st_kosov) + " stvari")


