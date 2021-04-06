a = int(input("Vnesi a")) # <- 
b = int(input("Vnesi b"))

# <, <=, >, >=, ==, !=

if a < b:
    print("a je manjši od b")
    print("A je še vedno manjši od b")
    print("A je še vedno manjši od b")
    print("A je še vedno manjši od b")
    print("A je še vedno manjši od b")
    print("A je še vedno manjši od b")
else:
    print("a ni manjši od b")


# Uporabnik naj vpiše številko meseca, mi pa mu odgovorimo s številom milisekund v mesecu
# Če pa je vpisal neki nesmiselnega ga pa opozorita in končajta program

# miliskeunde v dnevu
ur_v_dnevu = 24
mili_v_dnevu = ur_v_dnevu * 60 * 60 * 1000
# 86400000

if a == 3 or a == 4:
    print("A je 3 ali 4")

if a == 3 and a == 4:
    print("A je 3 in 4...., le kako je to mogoče")

mesec = 7
meseci_z_30 = [1, 3, 5, 7, 8, 10, 12]
if mesec in meseci_z_30:
    print(31)
elif mesec == 2:
    print("februar")
else:
    print("Nič od tega")

a = 10
b = 0

# %
# Napišita program, ki uporabnika povpraša po mesecu in letu ter mu pove število milisekund v tem mesecu








# Seznami
seznam = [1, 2, 3, 4, 5, 7, 200]
dolzina = len(seznam)
print(seznam[0]) # Prvi
print(dolzina - 1) # Zadnji
print(seznam[-2])# 
print(sedaj[dolzina - 2])






# Short circuit; to ima večina jezikov, tega nima pascal, večina jezikov to ima
x = [1, 2, 3]
if a > 0 and x [a]:
    pass
if b != 0 and a / b > 3:
    if a / b > 3:
        print("To je ziher ok")

if a > 10 or a*b > 200:
    print("to je večje")


