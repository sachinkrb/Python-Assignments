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
with open("employees_inverted.txt", "w") as output:
  json.dump(inverted_dict, output)
  
