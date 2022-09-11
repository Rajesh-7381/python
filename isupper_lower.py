data="Rajesh"
data23="raj  esh"
data12=" "
# alum=raj98
#it check letters are upper case or lower case
print(data.isupper())
print(data.islower())
# string convert into lower case
print(data.casefold())
# there is no space  so no error
print(data.isalpha())
#there is space so thats why it showing error
print(data23.isalpha())
print(data12.isspace())
#isalum function check it is alphanumeric or not
#it is not worked
#print(alum.isalum())