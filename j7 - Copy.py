
# This function will convert keys to values and vice versa.
# The values will be keys and the keys will group the previous keys
# if they are identical.
# This will be useful if we have to consider the values as keys. Its another way to group
# together similar keys in reference to the values in the whole data set provided.
# It is possible that there could be times when keys has to be used in programming
# as values while values might need to be converted to keys to determine duplicates or see
# what values are in common.
##def invert(d):
##  fopen = open('C:\\Users\\sachi\\Desktop\\employees.txt')
##  content = fopen.read()
##  words = content.split(":")
##  inverse = dict()
 
##
### Here the dictionary values are name:[Job,Salary,JobDuration,Hobby] respectively.
##employees = {
##  "David": ["Web Dev",4000,5,"Basketball"],
##  "Ali": ["Junior Java Dev",4000,3,"Football"],
##  "Ram": ["Senior Designer",5000,3,"Basketball"],
##  "Zustra": ["Help-Desk",2000,5,"Football"],
##  "Kobe": ["Manager",5000,1,"BasketBall"],
##}


import json #imported json to deserialize data(json objects to python objects)
def invert():
  inverse = dict()
  f = open('employees.txt') #The content of the file has been formatted to match JSON type.
  data=json.load(f) # This method will convert JSON into python objects.
  print("\nOriginal Dictionary:")
  for i in data["employees"]:
    print(i) # prints the content of employees as a dictionary.

    for key in i:
      val = i[key]
      for item in val:
        if item not in inverse:
          inverse[item] = [key]
        else:
          inverse[item].append(key)
    return inverse



inverted_dict=invert()
print("\nInverted Dictionary:")
print(inverted_dict)
