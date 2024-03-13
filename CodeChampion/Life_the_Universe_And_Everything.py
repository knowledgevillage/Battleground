print("Enter number of you choice ")

num_str_list=[]

print(type(num_str_list))
x=int(input("enter the first number"))
while x!=42:
    num_str_list.append(x)
    x=int(input("enter the next number"))

print("entered list is " , *num_str_list, sep="\n")