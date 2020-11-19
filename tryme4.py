# Implemented 4 different functions.
# Out of 4 , 3 functions are using nested function calls.
# It prints 9 lines with 9 dots and 25 lines with 25 dots with function calls.
def new_line():

    print('.') #Void function, doesn't return anything but prints.

def three_lines():
    
    new_line() #Calling another function called new_line().

    new_line()

    new_line()

def nine_lines():
    
    three_lines() #Calling another function called three_lines().

    three_lines()

    three_lines()
    
def clear_screen():
    
    nine_lines()  # Calling another function called nine_lines.
    nine_lines()
    three_lines()  #Calling another function called three_lines.
    three_lines()
    new_line()      #Calling another function called new_line.
    
print("Printing 9 lines:")

nine_lines() #Calling nine_lines() without arguments to print 9 lines.

print("Now printing 25 lines:") 

clear_screen() # Calling clear_screen() without arguments to print 25 lines.
