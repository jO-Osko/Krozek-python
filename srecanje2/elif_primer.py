n = 6
# Uporabnik naj vpiše n
# Izpisi prvega izmed 2,3 s katerim je deljivo

if n % 2 == 0:
    print("Deljiv je z 2")
elif n % 3 == 0:
    print("Deljiv je z 3")
elif n % 4 == 0:
    print("Deljiv je s 4")
else:
    print("Ni deljiv z nič od tega")

if n % 2 == 0:
    print("Deljiv je z 2")
else:
    if n % 3 == 0:
        print("Deljiv je z 3")
