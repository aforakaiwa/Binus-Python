x = int(input("Input age: ", ))
if (x > 0) and (x <= 1):
    print("Category: Baby")
elif (x >= 2) and (x <= 3):
    print("Category: Toddler")
elif (x >= 4) and (x <= 5):
    print("Category: Preschooler")
elif (x >= 6) and (x <= 12):
    print("Category: Child")
elif (x >= 13) and (x <= 17):
    print("Category: Teenager")
elif (x >= 18) and (x <= 21):
    print("Category: Young Adult")
elif (x >= 22) and (x <= 30):
    print("Category: Pre-adult")
elif (x >= 31) and (x <= 50):
    print("Category: Adult")
elif (x >= 51) and (x <= 70):
    print("Category: Preschooler")
elif (x >= 71):
    print("Category: Elderly")
else:
    print("Wrong input age")
