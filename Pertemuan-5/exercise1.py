def fungsiNama():
    print("""AFO RAKAIWA
PAMULANG\n""")
fungsiNama()

def fungsiTambah(value1=2, value2=3):
    result = value1 + value2
    return result

def fungsiKurang(value1=2, value2=3):
    result = value1 - value2
    return result
    
def fungsiBagi(value1=2, value2=3):
    result = value1 / value2
    return result
    
def fungsiKali(value1=2, value2=3):
    result = value1 * value2
    return result
    
def fungsiModulus(value1=2, value2=3):
    result = value1 % value2
    return result

#operator = "+" tidak perlu ternyata
while(True):
    operator = str(input("Enter Menu (+|-|/|*|%|stop):"))
    if(operator == "+" or operator == "-" or operator == "/" or operator == "*" or operator == "%"):
        x = int(input("Enter Value1: "))
        y = int(input("Enter Value2: "))
        if(operator == "+"):
            g_hasil = fungsiTambah(x, y)
            print("The result of addiction ",str(x)," + ",str(y)," is ",g_hasil)
        elif(operator == "-"):
            g_hasil = fungsiKurang(x, y)
            print("The result of substraction ",str(x)," - ",str(y)," is ",g_hasil)
        elif(operator == "/"):
            g_hasil = fungsiBagi(x, y)
            print("The result of division ",str(x)," / ",str(y)," is ",g_hasil)
        elif(operator == "*"):
            g_hasil = fungsiKali(x, y)
            print("The result of multiplication ",str(x)," * ",str(y)," is ",g_hasil)
        elif(operator == "%"):
            g_hasil = fungsiModulus(x, y)
            print("The result of modulus ",str(x)," % ",str(y)," is ",g_hasil)
        else:
            print("Program End")
    elif(operator != "stop"):
        print("Choose another menu")
    else:
        print("Program stopped. Thank you for using my program.")
        break
    
