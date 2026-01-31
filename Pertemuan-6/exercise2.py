class Student:
    def __init__(self, name="None", score=0):
        self.name = name
        self.score = score
        
    def getName(self):
        return self.name
        
    def getScore(self):
        return self.score
        
    def setName(self, name):
        self.name = name
        
    def setScore(self, score):
        self.score = score
    
def banner():
    print("""===== OOP Program =====
1. Declare Object
2. Display Object
3. Change Object Value
4. Delete Object
5. Exit Program
""")

student1 = Student()

while (True):
    banner()
    menu = str(input("Enter Your Choice (1/2/3/4/5): "))
    
    if(menu == "1"):
        name = str(input("Input Nama: "))
        score = int(input("Input Score: ",))
        print("")
        student1 = Student(name,score)
        
    elif(menu == "2"):
        name = student1.getName()
        score = student1.getScore()
        
        print("Name:", name)
        print("Score:", score)
        print("")
    
    elif(menu == "3"):
        change = str(input("Menu to Change (name/score): " ))
        if (change == "name"):
            name = student1.setName(str(input("Change Name: ")))
        elif (change == "score"):
            score = student1.setScore(int(input("Change Score:")))
        else:
            print("Wrong menu")
        print("")
    
    elif(menu == "4"):
        student1 = Student("None",0)
        print("Data Deleted")
    
    elif(menu == "5"):
        print("Exit program. Thank you")
        break
    
    else:
        print("Wrong menu")
