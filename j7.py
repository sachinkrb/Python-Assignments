
# This function will convert keys to values and vice versa.
# The values will be keys and the keys will group the previous keys
# if they are identical.
# This will be useful if we have to consider the values as keys. Its another way to group
# together similar keys in reference to the values in the whole data set provided.
# It is possible that there could be times when keys has to be used in programming
# as values while values might need to be converted to keys to determine duplicates or see
# what values are in common.
def invert(d):
  inverse = dict()
  for key in d:
    val = d[key]
    for item in val:
      if item not in inverse:
        inverse[item] = [key]
      else:
        inverse[item].append(key)
  return inverse 

# Here the dictionary values are name:[Job,Salary,JobDuration,Hobby] respectively.
employees = {
  "David": ["Web Dev",4000,5,"Basketball"],
  "Ali": ["Junior Java Dev",4000,3,"Football"],
  "Ram": ["Senior Designer",5000,3,"Basketball"],
  "Zustra": ["Help-Desk",2000,5,"Football"],
  "Kobe": ["Manager",5000,1,"BasketBall"],
}
print("Original Dictionary:")
print(employees)
inverted_employees= invert(employees)
print("Inverted Dictionary:")
print(inverted_employees)
print(invert({"1": "10", "2": "10", "3": "20"}))
