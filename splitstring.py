long_string = "This is going to be a very long string"
print(long_string)
split_string = long_string.split()
print(split_string)
#pop
split_string.pop(6)
print("After using pop method :\n",split_string)
#del
del split_string[6]
print("After using del operator :\n",split_string)
#remove
split_string.remove('This')
print("After using remove method :\n",split_string)
#sort
split_string.sort()
print("After using sort method :\n",split_string)
#append
split_string.append("doesn't")
print("After using append method :\n",split_string)
#extend
temp_list = ["make","any","sense"]
split_string.extend(temp_list)
print("After using extend method :\n",split_string)
#+ operator
temp_list2 = ["cuckoo"]
split_string_final = split_string + temp_list2 
print("After using + operator :\n",split_string_final)
#join
delimiter = ' '
final_string = delimiter.join(split_string_final)
print("After using join method :\n", final_string)
