try:
    number = int(input("Enter a number:"))
    sumatory = 0
    for i in range(number + 1):
        sumatory += i
    
    print('The sum of all numbers is', sumatory)
except:
    print('You have not entered a correct number, please try again.')  
