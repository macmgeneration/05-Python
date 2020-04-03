def print_triangular_numbers(n):
    if n <= 0:
        return
    for i in range(1, n + 1):
        print(i, (i * (i + 1)) // 2)


number = int(input('Enter a number: '))
print_triangular_numbers(number)
