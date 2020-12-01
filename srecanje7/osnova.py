
ime = "AHAHAHAHAHAHA"

skupna_starost = 0

output_file = open("podatki.txt", "w")

while ime != "":
    ime = input("Vnesi ime")
    if ime == "":
        break
    starost_v_mesecih = int(input("Vnesi starost v mesecih"))
    skupna_starost += starost_v_mesecih

    output_vrstica = ime + ", " + str(starost_v_mesecih) + "\n"

    output_file.write(output_vrstica)

    print("Pozdravljen:", ime, "star si:", starost_v_mesecih/12)

print("Skupaj so stari:", skupna_starost/12, "let")


output_file.close()

# Odpreš datoteko

# Pišeš kar želiš

# Datoteko zapreš

