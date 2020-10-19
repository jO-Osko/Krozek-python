# Uporabnik napiše svoje ime
# Uporabnik naj vpiše koliko bonbonov ima s številko

# Izpišemo: Uporabnik ima VPISANO bonbonov
# Zadnjo cifro dobimo kot
# n % 10
# 81 bonbonov in ne 81 bonbon
beseda = "bonbon"
ime = input("Vnesi svoje ime:")
n = int(input("Vnesi število bonbonov:"))

# Določimo pripono glede na sklon in števnik
if n % 100 == 1:
    pripona = ""
if n % 100 == 2:
    pripona = "a"
if (n % 100 == 3) or (n % 100 == 4):
    pripona = "e"
else:
    pripona = "ov"


# Izpišemo vse skupaj s pripono    
print(ime + " ima " + str(n) + beseda + pripona)





