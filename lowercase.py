##def any_lowercase1(s):
##     for c in s:
##          if c.islower():
##               return True
##          else:
##               return False
##print(any_lowercase1("aBC"))
##print(any_lowercase1("Abc"))

##              
##def any_lowercase2(s):
##     for c in s:
##          if 'c'.islower():
##               return 'True'
##          else:
##               return 'False'
##print(any_lowercase2("aBC"))
##print(any_lowercase2("Abc"))
##print(any_lowercase2("ADAsdadaSE"))
##
##def any_lowercase3(s):
##     for c in s:
##          flag = c.islower()
##     return flag
##print(any_lowercase3("aBC"))
##print(any_lowercase3("aBc"))

##print(any_lowercase3("ADAsdadaSE"))
##
##def any_lowercase4(s):
##     flag = False
##     for c in s:
##          flag = flag or c.islower()
##     return flag
##print(any_lowercase4("aBC"))
##print(any_lowercase4("aBc"))
##print(any_lowercase4("ABC"))
##print(any_lowercase4("abc"))
##print(any_lowercase4("abC"))
##print(any_lowercase4("aBc"))
##
##def any_lowercase5(s):
##     for c in s:
##          if not c.islower():
##               return False
##     return True
##print(any_lowercase5("AbC"))
##print(any_lowercase5("aBc"))
##print(any_lowercase5("ABC"))
##print(any_lowercase5("abc"))
##print(any_lowercase5("abC"))
##print(any_lowercase5("aBc"))
##print(any_lowercase5("ADAsdadaSE"))
##
##def any_lowercase5(s):
##     for c in s:
##          if c.islower():
##               return True
##     return False
##print(any_lowercase5("AbC"))
##print(any_lowercase5("aBc"))
##print(any_lowercase5("ABC"))
##print(any_lowercase5("abc"))
##print(any_lowercase5("abC"))
##print(any_lowercase5("aBc"))
def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True
print(any_lowercase5("AbC"))
print(any_lowercase5("aBc"))
print(any_lowercase5("ABC"))
print(any_lowercase5("abc"))
print(any_lowercase5("abC"))
print(any_lowercase5("aBc"))
