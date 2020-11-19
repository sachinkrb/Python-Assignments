###Example 1 => Trying to open a file that doesn't exist.
##try:
##    finput = open('secfile')
##except:
##    print('Not able to find this file')
##
###Example 2 => The directory 'Python Task' doesn't exist.   
##try:
##    finput = open('C:\\Users\\sachi\\Desktop\\Python Task')
##except:
##    print('No such file or directory exists')
##
##
###Example 3 => Access denied for this directory.
##try:
##    finput = open('C:\\Users')
##    
##except:
##    print("Permission denied for this directory")
##    
import os
cwd = os.getcwd()
os.path.exists(cwd)
try:
    fin = open('answer.txt')
    fin.write('Yes')
except:
    print('No')
print('Maybe')
