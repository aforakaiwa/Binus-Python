import math
A = float(input("Nilai a : "))
B = float(input("Nilai b : "))
C = float(input("Nilai c : "))
D = (B**2) - (4*A*C)
print("Nilai Diskriminan = ",D)

if A == 0:
    print("It is not a quadratic equation")
elif D > 0:
    print("It has distinct roots")
    print(A, "x²+", B,"x+", C)
    print("Nilai Diskriminan = ",D)
    x1 = (-B + math.sqrt(D)) / 2*A
    x2 = (-B - math.sqrt(D)) / 2*A
    print("x1 = ", x1)
    print("x2 = ", x2)
elif D < 0:
    print("It has imaginary roots")
    print(A, "x²+", B,"x+", C)
    print("Nilai Diskriminan = ",D)
    print("x1,2 = (", -B, "±", round(math.sqrt(abs(D)),2), "i", ") /", 2*A)
else: 
    D == 0
    print("It has double roots")
    print(A, "x²+", B,"x+", C)
    print("Nilai Diskriminan = ",D)
    x1 = (-B / 2*A)
    print("x1,2 = ", x1)
