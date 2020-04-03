try:
    number = int(input("Enter a number:"))
    sumatory = 0
    for i in range(number + 1):
        if i % 2 == 0 : sumatory += i
    
    print('The sum of even numbers is', sumatory)
except:
    print('You have not entered a correct number, please try again.')  
