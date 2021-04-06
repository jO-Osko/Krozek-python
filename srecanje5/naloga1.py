# Zaokrozevanje

# Zaokrožit moram tako, da se X.5 zaokroži navzgor
# ostalo pa na najbližjo število
# Imamo C.D

# Večino časa bo odgovor število 
# C, včasih 
# C + 1; včasih 
# C - 1

def zaokrozi(x):
    c = odrezi(x)
    if (x - c) >= 0.5:
        c += 1
    elif (x - c) <= -0.5:
        c -= 1
    if c == 0 and x <= 0:
        return -0.0
    return c


