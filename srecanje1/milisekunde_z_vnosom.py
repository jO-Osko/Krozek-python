vnos_uporabnika = int(input("Vnesi število ur v dnevu:"))
vnos_uporabnika2 = int(input("Vnesi število dni v mesecu:"))

st_ur = vnos_uporabnika
st_dni = vnos_uporabnika2
st_minut_v_uri = int(input("Vnesi število minut v uri"))
st_sekund_v_minuti = int(input("Vnesi število sekund v minuti"))
st_milisekund = int(input("Vnesi število milisekund v sekundi"))

max_milisekund = int(input("Koliko je največje število milisekund v mesecu?"))

zacetni_pozdrav = "Stevilo milisekund v marcu je:"
koncni_pozdrav = "Adijo"

stevilo_vseh_milisekund = st_dni * st_ur *  st_minut_v_uri * \
      st_sekund_v_minuti *  st_milisekund

# Izpise stvari
print(zacetni_pozdrav)
print(stevilo_vseh_milisekund)

if stevilo_vseh_milisekund > max_milisekund:
    print("Delaš nadure")
    print("Pazi da ne boš preveč utrujen")
    print("nadure")
else:
    print("Delaš premalo")
    print("Nisi dovolj delaven....")


print("Adijo")