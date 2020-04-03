def sum_to(n):
    sumatory = 0
    for i in range(n + 1):
        sumatory += i
    return sumatory

num = int(input('Enter a number: '))
print('The sum is: ', sum_to(num))