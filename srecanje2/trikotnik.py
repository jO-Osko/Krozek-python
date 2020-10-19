# Prebere tri številke od uporabnika
# a, b, c
# Preveri, če te stranice predstavljajo stranice nekega trikotnika

a = float(input("vnesi stranico a"))
b = float(input("vnesi stranico b"))
c = float(input("vnesi stranico c"))

if a+b > c and a + c > b and b +c > a:
    print("Je trikotnik")
    s = (a + b + c)/2
    pl = s*(s-a)*(s-b)*(s-c)
    print("ploščina je: " + str(s**0.5))
    print("obseg je: " + str(2*s))
else:
    print("To ni trikotnik")