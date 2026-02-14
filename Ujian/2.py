print("2.a. Variabel merupakan suatu wadah untuk menyimpan data, baik berupa Angka, Nilai, dan/atau Hasil Perhitungan\n")

print("2.b. y2h, _t, x\n")

print("2.c.")
print("nilai y2h belum didefiniskan di awal")
print("x % 2 = 1 seharusnya ditulis x % 2 == 1")
print("range(5) berarti x akan bernilai 0,1,2,3,4. Jika _t > x terpenuhi dan jika x = 0, maka akan terjadi pembagian oleh 0 dan terjadi error 'ZeroDivisionError: integer division or modulo by zero'\n")

y2h = 0
_t = 18
for x in range(1,5):
    if x % 2 == 1:
        y2h = _t - x
    elif _t > x:
        _t = _t // x
    else :
        y2h = y2h + 1
    print (x , y2h)
