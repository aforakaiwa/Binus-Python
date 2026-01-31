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

student1 = Student(str(input("Input Nama: ")), str(input("Input NISN: ")), str(input("Input Tempat Lahir: ")), str(input("input Tanggal Lahir: ")))
print("\n")

student1.printStudent()
student1.displayCount()
