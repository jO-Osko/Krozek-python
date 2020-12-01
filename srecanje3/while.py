stevilo = int(input("Vnesi stevilo:"))
napacni_vpisi = 0

while stevilo > 3:
    print(stevilo)
    print("Tole pa ni manjše od 3")

    stevilo = int(int(input("Vnesi število:")))
    napacni_vpisi += 1

print("Končno si vpisal nekaj kar ni večje od 3")
print("Zmotil si se", napacni_vpisi, "krat")
