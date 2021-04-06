seznam_imen = [
    "Filip", "Miha", "Luka", "Martin", "Krisofer", 
    "Maja", "Maja", "Maja"
]

iskano_ime = "Majaxyz"

index_imena = 0

se_iscem = True

while index_imena < len(seznam_imen):

    trenutno_ime = seznam_imen[index_imena]

    if trenutno_ime == iskano_ime:
        print("Nasel sem ga, je na mestu", index_imena)
        break
        se_iscem = False

    index_imena += 1 # -= *= /= %=

if se_iscem:
    print("Nisem našel iskanega")


