i = "Y"

while(True):
    if(i == "Y"):
        sideA = float(input("Side A: "))
        sideB = float(input("Side B: "))
        sideC = float(input("Side C: "))

        if ( sideA == sideB == sideC):
            print("Segitiga Sama Sisi")
        elif (sideA == sideB) or (sideA == sideC) or (sideB == sideC):
            print("Segitiga Sama Kaki")
        elif (sideA**2 + sideB**2 == sideC**2) or (sideA**2 + sideC**2 == sideB**2) or (sideB**2 + sideC**2 == sideA**2):
            print("Segitiga Siku-siku")
        elif (sideA + sideB <= sideC) or (sideA + sideC <= sideB) or (sideB + sideC <= sideA):
            print("Bukan Segitiga")
        else:
            print("Segitiga Sembarang")
    else:
        print("Program was End")
        break
    i = str(input("Do you want to repeat: "))
        
    
    
