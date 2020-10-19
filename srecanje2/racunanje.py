a = int(input("vnesi a:"))
b = int(input("vnesi b:"))

# Če je katerikoli izmed a in b manjši od 0 potem -> nekej
# drugače poračunaj

if a > 0 and b > 0:
    c = (a ** 2 + b ** 2) ** 0.5
    print("c = " + str(c))
else:
    print("Neveljaven trikotnik")

if a <= 0 or b <= 0:
    print("Neveljaven trikotnik")
else:
    c = (a ** 2 + b ** 2) ** 0.5
    print("c = " + str(c))

