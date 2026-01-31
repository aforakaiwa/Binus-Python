class Student:
    "Common base class for all students"
    stuCount = 0
    
    def __init__(self, name="Student", nisn="0", tempatLahir = "Jakarta", tanggalLahir="01 Januari 2000"):
        self.name = name
        self.nisn = nisn
        self.tempatLahir = tempatLahir
        self.tanggalLahir = tanggalLahir
        Student.stuCount += 1
        
    def displayCount(self):
        print("Total Students: %d" % Student.stuCount)
    
    def printStudent(self):
        print("Name:", self.name, "\nNISN:", self.nisn, "\nTempat Lahir: ", self.tempatLahir, "\nTanggal Lahir: ", self.tanggalLahir)

name = str(input("Input Nama: "))
nisn = str(input("Input NISN: "))
tempatLahir = str(input("Input Tempat Lahir: "))
tanggalLahir = str(input("input Tanggal Lahir: "))
student1 = Student(name, nisn, tempatLahir, tanggalLahir)
print("\n")

student1.printStudent()
student1.displayCount()
