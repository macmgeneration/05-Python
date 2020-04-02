largest = -1
while True:
    try:
        str = input("Enter a number (# to exit):")
        if str == "#":
            break;
        number = int(str)
        if largest < number:
            largest = number
        
    except:
        print('You have not entered a correct number, please try again.')  

print('The largest number is ', largest)
