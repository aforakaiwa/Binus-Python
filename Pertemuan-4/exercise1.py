temp = ""
i = 0
j = 0
a = int(input("Input Max Value: "))
for i in range(a):
    temp = str(a)
    for j in range(a, 1, -1):
        temp = temp + str(a)
    print (temp)
    a -= 1
