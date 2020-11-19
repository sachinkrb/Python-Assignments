def my_sqrt(a):

    x = 0.1 #base

    while True:

         y = (x + a/x) / 2.0

         if y == x:

              break

         x = y

    return x

my_sqrt(100)

 

import math

a = 1

while a <= 9:

    diff = abs(my_sqrt(a) - math.sqrt(a))

    print(f"a = {a} | my_sqrt(a) = {my_sqrt(a)} | math.sqrt(a) = {math.sqrt(a)} | diff = {diff}  ")

    a = a + 1

import math

a = 1

while a <= 25:

    diff = abs(my_sqrt(a) - math.sqrt(a))

    print(f"a = {a} | my_sqrt(a) = {my_sqrt(a)} | math.sqrt(a) = {math.sqrt(a)} | diff = {diff}  ")

    a = a + 1
