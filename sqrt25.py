import math
def my_sqrt(a): # my_sqrt function that takes one argument
    x = 1   # initializes x
    while True:        
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return y # returns final value

def test_sqrt():
    for a in range(1,26):
        mysqrt = my_sqrt(a) # calls my_sqrt function
        mathsqrt = math.sqrt(a) # calls math module 
        diff = abs(mathsqrt - mysqrt) # calculates absolute values
        # print values of a, my_sqrt of a , math.sqrt of a
        # and their absolute differences
        print("a =",a," | my_sqrt(a) =",mysqrt," | math.sqrt(a) =",mathsqrt," | diff =",diff)
test_sqrt() 
