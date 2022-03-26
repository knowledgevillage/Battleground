# take user input

from imp import init_builtin





#print(init_number)

try:
    init_number=int(input("Enter the number")) #take the input and convert that into integer
    print(init_number)
    reverse_number=0
    while init_number !=0:
        reverse_number=init_number%10+reverse_number*10 
        init_number=init_number//10
    print("the reversed number is ",reverse_number)
except ValueError:
    print("PLease enter the number values from [0-9]")