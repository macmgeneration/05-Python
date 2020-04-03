def computepay(hours, rate):
    if hours > 40:
        return (40 * rate + (hours - 40) * (rate * 1.5))
    else:
        return (hours * rate)

hours = int(input('Enter hours: '))
rate = float(input('Enter rate: '))

print('The total is ', computepay(hours, rate))