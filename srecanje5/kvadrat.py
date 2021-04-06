# Uporabnik vnese stevilo n
# izpisi kvadrat n*n iz samih X

#n = int(input("Vnesi velikost"))

#for vrstica in range(n):
#    print(n * "X")


crke = "abcdefghijklmnopqrstuvwxyz"

id_crke = {}
crke_id = {}
for j in range(len(crke)):
    id_crke[crke[j]] = j + 1
    crke_id[j] = crke[j] # Namesto tega bi lahko uporabil kar crke
    # "a" -> 0
    # "z" -> 25

id_crke = {
    crke[j]:j for j in range(len(crke))
}


print(id_crke)
print(id_crke["g"])