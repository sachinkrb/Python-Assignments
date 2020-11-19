alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

    
# Part 1: To test if there is a duplicate in alphabet variable.

def has_duplicates(s): # Returns True for having duplicates else false.
    d = histogram(s) # Converts to dictionary.
    for k in d:
        if d[k] > 1:
            flag = True
            break   # Exits out to return flag if it hits True.
        else:
            flag = False
    return flag
print(has_duplicates(alphabet)) # Check to see if there are duplicates.


# Part 1: for loop to iterate over test_dups list.

for e in test_dups:
    if has_duplicates(e):
        print(e,"has duplicates")
    else:
        print(e,"has no duplicates")

#Part 2. Checks for alphabets not in the string.   
def missing_letters(s):
    for y in s:
        alpha_list = list(alphabet)
        for x in histogram(y):
            if x in alpha_list:
                alpha_list.remove(x)
        new_list=''.join(alpha_list)
        if new_list == '': 
            print(y + " uses all the letters")
        else:
            print(y + " is missing letters",new_list)
missing_letters(test_miss)

