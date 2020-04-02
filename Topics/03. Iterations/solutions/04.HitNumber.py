import random
rng = random.Random()
numAleatorio = rng.randrange(1,1000)

print('----------------------------')
print('----- HIT THE NUMBER ------')
print('----------------------------')
print('')
print('(input # to exit)')

while True:
    try:
        str = input("Enter a number:")
        if str == "#":
            print('You have given up !!. You will be left with the doubt of what it was')
            break
        test = int(str)
        if test > numAleatorio:
            print('The number entered is greater. Keep trying')
        elif test < numAleatorio:
            print('The number entered is less. Keep trying')
        else:
            print('!! Congratulations!! You have guessed the number', numAleatorio)
            break
    except:
        print('You have not entered a correct number, please try again.')  
