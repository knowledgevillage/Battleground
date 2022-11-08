def take_input():
    try:
        no_of_test_cases=int(input("Enter the number of test cases you want to run between 0 to 10"))
        if no_of_test_cases not in (1,10):
            print('Invalid entry')
            exit
    except:
        print("Invalid literal")
        exit


if __name__=="__main__":
    take_input()