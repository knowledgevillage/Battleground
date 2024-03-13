#check if the user input is a amstorong number or not

#ask for the user input


from traceback import print_tb


try:
    raw_input = int(input("enter a number "))
    valid_input=raw_input
    val_num=0

    while raw_input!=0:
        val_num=pow((raw_input%10),3)+val_num
        print(val_num)
        raw_input=raw_input//10

    print("raw_input =", raw_input)
    print("valid_input =", valid_input)
    print("val_num = ", val_num)
    if valid_input==val_num:
        print(valid_input, "is a amstrong number")
    else:
        print(valid_input, " is not a amstrong number")

except ValueError:
    print("please enter the digites from [0-9]")

