# Navodila
# Program naj uporabnika vpraša po imenu
# Program naj izpiše "Pozdravljen IME_UPORABNIKA!"
# Program naj izpiše "Adijo IME_UPORABNIKA!"
ime = input("Kakšno je tvoje ime:")

IME_SEFA = "Janez"

print("Pozdravljen " + ime)
# Poseben pozdrav za šefa
if ime.lower() == IME_SEFA.lower():
    print("Ti si šef: " + ime.title())

print("Adijo " + ime)

