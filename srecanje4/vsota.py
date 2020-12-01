# Domača naloga

# Uporabnik naj vpiše število
# Izpiši vsoto njegovih števk

# 14678324
# 1467832 -> 1467832_4
# -14678324
stevilo = int(input("Vnesi število"))

vsota = 0
if stevilo < 0:
    stevilo = stevilo * -1
# stevilo = abs(stevilo)

while stevilo != 0:
    print("Število:", stevilo)
    zadnja_stevka = stevilo % 10
    vsota += zadnja_stevka

    # // deli celoštevilsko, torej nam ne da decimalk

    stevilo = stevilo // 10

print("Vsota števk:" + str(vsota))