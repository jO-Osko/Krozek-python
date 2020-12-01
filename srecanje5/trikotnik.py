# Uporabnik vnese stevilo n
# izpisi trikotnik 
# X
# XX
# XXX
# XXXX
# XXXXX

n = 5
# n = int(input("Vnesi velikost"))
znak = "A"
# znak = input("Vnesi znak:")
znak_presledek = "."

for st_vrstice in range(n):
    break
    print((st_vrstice + 1) * znak)

# dvojni
num = 5
for add in range(0, num, 2):
    for vrstica in range(n):
        print(znak_presledek*(n-vrstica - 1 + num//2 - add//2) + znak*(2*vrstica+1 + add))

##### ......A
......A 
.....AAA
....AAAAA
...AAAAAAA
..AAAAAAAAA
.....AAA
....AAAAA
...AAAAAAA
..AAAAAAAAA
.AAAAAAAAAAA
....AAAAA
...AAAAAAA
..AAAAAAAAA
.AAAAAAAAAAA
AAAAAAAAAAAAA
