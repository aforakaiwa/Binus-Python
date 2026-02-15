dataDict = {}

def tambah_mahasiswa():
    nama = input("Nama mahasiswa: ")
    nilai_list = []
    while True:
        nilai = input("Nilai ('stop' untuk selesai): ")
        if nilai == "stop":
            break
        nilai_list.append(int(nilai))
    dataDict[nama] = nilai_list
    print("Data berhasil ditambahkan.\n")

def rerata_nilai_mhs(nama, data):
    nilai_list = data.get(nama)

    if nilai_list is None:
        print("Data mahasiswa tidak ditemukan")
        return
    temp = ""
    for n in nilai_list:
        temp = temp + str(n) + " "
    print(temp)
    total = 0
    jumlah = 0

    for n in nilai_list:
        total += n
        jumlah += 1

    rerata = total / jumlah
    print("Rerata =", int(rerata))

while True:
    print("=== MENU ===")
    print("1. Tambah mahasiswa")
    print("2. Tampilkan nilai & rerata")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_mahasiswa()

    elif pilih == "2":
        nama = input("Masukkan nama mahasiswa: ")
        rerata_nilai_mhs(nama, dataDict)
        print()

    elif pilih == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.\n")
