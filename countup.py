def countup(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          countup(1+n)
          
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

# Please enter a positive number to invoke countup function.
# Please enter a negative number to invoke countdown function.

count = int(input("Please enter a number\n")) # Gets input by creating newline(\n) and converts to int type.
if count >= 0: #Doesn't matter if your input is equal to zero for countup or countdown.
    countdown(count) # Calling countdown function
else:
    countup(count)      #Calling countup function

