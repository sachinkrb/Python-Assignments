### Tuples can be useful to combine strings and lists together to produce tuples.
### We can do so by using the zip function. The final result of combining lists
### and strings will be a tuple type.
### We can also use zip function inside list function to contain tuples
### inside a list.
### We can use for loop to traverse a list of tuples as well.
##seq = '123'
##veg_mix = ['beetroot', 'carrot', 'cucumber']
##mix_with =['pineapple','banana','cherry']
##more_fruit =['apple', 'mango','grapes']
##into_list = list(zip(seq, veg_mix, mix_with, more_fruit))
##print("Example of tuples inside a list:")
##print(into_list)
##print("Example of 'zip' function:")
##for smoothie in zip(seq, veg_mix, mix_with, more_fruit):
##    print(smoothie)
##    print(type(smoothie))
##print("Example of traversing through a list of tuples:")
##for n,veg,fruit1,fruit2 in into_list:
##    print(n,veg,fruit1,fruit2)
##    
### We can also us built in enumerate function which will iterate through
### lists or string and index it.
##
##print("Example for 'enumerate' function:")
##for index, element in enumerate(veg_mix):
##    print(index, element)
##
### We can use built-in 'items' function to return a sequence
### of tuples from a dictionary.
##
##d_form = {'apple':1, 'banana':2, 'carrot':3}
##t_form = d_form.items()
##print(t_form)
seq = '123'
veg_mix = ['beetroot', 'carrot', 'cucumber']
mix_with =['pineapple','banana','cherry']
more_fruit =['apple', 'mango','grapes']
into_list = list(zip(seq, veg_mix, mix_with, more_fruit))
print("Example of tuples inside a list:")
print(into_list)
print("Example of 'zip' function:")
for smoothie in zip(seq, veg_mix, mix_with, more_fruit):
    print(smoothie)
    print(type(smoothie))
print("Example of traversing through a list of tuples:")
for n,veg,fruit1,fruit2 in into_list:
    print(n,veg,fruit1,fruit2)
