try:
    number = int(input("Enter a number:"))
    counter = 0
    for i in range(number + 1):
        if i % 2 == 1 : counter += 1
    
    print('There are ', counter, ' odd numbers')
except:
    print('You have not entered a correct number, please try again.')  
