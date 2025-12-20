import math
sideA = float(input("Side A: "))
sideB = float(input("Side B: "))
sideC = float(input("Side C: "))

allSide = sideA + sideB + sideC
maxLenght = max(sideA, sideB, sideC)
print(maxLenght)
allSide - max(sideA, sideB, sideC) > max(sideA, sideB, sideC) == True

sudutA = math.sin(sideA / sideB)
sudutB = math.sin(sideA / sideC)
sudutC = math.sin(sideB / sideC)

if ( sideA == sideB == sideC):
    print("Segitiga Sama Sisi")
elif (sideA == sideB) or (sideA == sideC) or (sideB == sideC):
    (sudutA == sudutB) or (sudutA == sudutC) or (sudutB == sudutC)
    print("Segitiga Sama Kaki")
elif (allSide - max(sideA, sideB, sideC) <= max(sideA, sideB, sideC)):
    print("Bukan Segitiga")
else:
    print("Segitiga Sembarang")
