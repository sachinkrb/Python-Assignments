def grades_readable(grade): #accepts a grade as a numeric value and returns the letter grade
    if type(grade) != int: #in case the user does not type well
        print("Only numbers please.")
    elif grade < 60 >= 0:
        print("This grade is an F.")
    elif grade < 70:
        print("This grade is a D.")
    elif grade < 80:
        print("This grade is a C.")
    elif grade < 90:
        print("This grade is a B.")
    elif grade <= 100:
        print("This grade is an A")
    else: #catches out of scale or other possible number errors
        print("That entry is invalid. Try again.")
