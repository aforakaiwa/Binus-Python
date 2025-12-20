print ("Pilihan konversi:\n1. Celcius to Fahrenheit\n2. Celcius to Kelvin\n3. Fahrenheit to Celcius\n4. Fahrenheit to Kelvin\n5. Kelvin to Celcius\n6. Kelvin to Fahrenheit\n")
x = float(input("Input nilai suhu awal: "))
y = int(input("Nomor pilihan konversi (1-6): "))
if (y == 1):
    print("Celcius to Fahrenheit")
    z = ((9/5)*x) + 32
    print("Hasilnya ", z, "F")
elif (y == 2):
    print("Celcius to Kelvin")
    z = x + 273
    print("Hasilnya ", z, "K")
elif (y == 3):
    print("Fahrenheit to Celcius")
    z = (x - 32) * (5/9)
    print("Hasilnya ", z, "C")
elif (y == 4):
    print("Fahrenheit to Kelvin")
    z = ((x - 32) * (5/9)) + 273
    print("Hasilnya ", z, "K")
elif (y == 5):
    print("Kelvin to Celcius")
    z = x - 273
    print("Hasilnya ", z, "C")
elif (y == 6):
    print("Kelvin to Fahrenheit")
    z = ((9/5)*(x-273)) + 32
    print("Hasilnya ", z, "F")
else:
    print("Pilihan konversi salah")
