# Sprasuj uporabnika po stevilkah in jih 
# dodajaj v seznam dokler ni 0

seznam_stevil = []

vpisano_stevilo = int(input("Vnesi stevilo"))

stevilo_vpisanih = 1

while stevilo_vpisanih != 10 and vpisano_stevilo != 0:
    # Enako kot pri if stavku
    # zamaknemo stvari noter
    seznam_stevil.append(vpisano_stevilo)
    stevilo_vpisanih = stevilo_vpisanih + 1
    vpisano_stevilo = int(input("Vnesi stevilo"))

print("Vpisal si števila")
print(seznam_stevil)


