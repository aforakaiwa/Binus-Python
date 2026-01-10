temp = ""
i = 0
j = 0
a = int(input("Input Max Value: "))
for i in range(a, 0, -1):
    for j in range(0, i, 1):
        temp = temp + str(i)
    temp = temp + "\n"

for i in range(2, a+1, 1):
    for j in range(0, i, 1):
        temp = temp + str(i)
    temp = temp + "\n"
    
print (temp)
