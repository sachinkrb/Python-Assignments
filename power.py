def is_divisible(a,b):
    if a % b != 0: #checks the base case to see if the number is divisible.
        return False
    else: 
        return True
def is_power(a,b):
    if a == b or b == 1: #Checks for base case for two arguments being equal or 1.
        return True
    else:
        if is_divisible(a,b): #Calls is_divisible function.
            return is_power(a/b, b) #Calls is_power function recursively.
        else:
            return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

