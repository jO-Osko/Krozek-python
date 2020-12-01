# Uporabnik vnese številko

# Če je število deljivo s 3 naj izpiše "fizz"
# Če je deljivo s 5 naj izpiše "buzz"
# če je deljivo z obema naj izpiše "fizz buzz"
# Drugače naj izpiše samo to število




zacetno_stevilo = int(input("Vnesi začetno število:"))
koncno_stevilo = int(input("Vnesi število s katerim naj konča:"))

print("ZACETEK")
# range(1, 10) # -> 1, 2, 3, 4, 5, 6, 7, 8, 9 
# range(1, 12, 3) ->  1, 4, 7, 11, ...
# Isto, tudi ce bi tukaj preimenoval v stevilo
for stevilo in range(zacetno_stevilo, koncno_stevilo + 1, 4): # 1, 2, 3, 4
    if stevilo % 3 == 0 and stevilo % 5 != 0:
        print("Fizz")
    elif stevilo % 5 == 0 and stevilo % 3 != 0:
        print("Buzz")
    elif stevilo % 3 == 0 and stevilo % 5 == 0:
        print("Fizz Buzz")
    else:
        print(stevilo)

print("KONEC")
