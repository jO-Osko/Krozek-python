# Evklidov algoritem
# INPUT: Dve naravni števili: a in b
# OUTPUT: največji skupni delitelj števil a in b

x = 2*3*3*  5
y =   3*3*3*5*5

##### Evklidov algoritem

def gcd(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c 
        c = a % b

    return b

def gcd_seznama(sez):
    # Funkcija dobi seznam celih števil in vrne gcd tega seznama
    
    # V "g" si bomo shranili gcd do sedaj

    g = sez[0]
    # gremo po vrsti in popravljamo "g"
    for i in range(1, len(sez)):
        g = gcd(g, sez[i])

    return g

def lcm(a,b):
    return a*b // gcd(a,b)

def lcm_seznama(sez):
    v = sez[0]

    for i in range(1, len(sez)):
        v = lcm(v, sez[i])
    
    return v


rezultat = gcd(x, y)
print(gcd_seznama([15, 45, 25]))

print("v: 15, 25 je ", lcm(15, 25))
print(lcm_seznama([15, 45, 25]))
#### Konec algoritma, nastavi rezultat na pravilno stvar

# rezultat mora biti 5
print(rezultat)