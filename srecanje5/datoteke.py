f = open("input.txt", "w")
f.write("Prva vrstica\n")
f.write(str(1+ 10) + "\n")

f.close()

# Beremo na več načinov
# Prebereš celega
# cel_file = f.read()
# print(cel_file)

# Vrstico po vrstico
#prva_vrstica = f.readline()
"""
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline()) # Ko je file "prazen" readline() vrne ""
print(f.readline()) # Ko je file "prazen" readline() vrne ""
print(f.readline()) # Ko je file "prazen" readline() vrne ""
"""

"""
vse_vrstice = f.readlines()
print(vse_vrstice)
"""
"""
vsota = 0
for vrstica in f:
    print(vrstica.split(","))

print(vsota)
"""

f.close()