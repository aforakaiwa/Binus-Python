i = "Y"

while(True):
    if(i == "Y"):
        a = int(input("Angka: "))
        if(a%2 == 0):
            print ("The number ", a, "is Even")
        else:
            print ("The number ", a, "is Odd")
    else:
        print("Program was End")
        break
    i = str(input("Do you want to repeat: "))
