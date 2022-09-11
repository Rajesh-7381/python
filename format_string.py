age=38
txt="my name is rajesh,i am age:{}"
# it gives error
#print(txt)
print(txt.format(age))


# the format method take unlimited no. of argument
quantity=3
item_no=234
price=64.83
myorder="i want {} pieces of item {} for {} rupees."
print(myorder.format(quantity,item_no, price))

# also we an print using index number
myorder="i want to pay{2} dollars for{0} pieces of item{1}"
print(myorder.format(quantity,item_no, price))

