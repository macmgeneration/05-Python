while True:
    try:
        hours_str = input("Enter Hours: ")
        hours = float(hours_str)
        break
    except:
        print("Error, please enter numeric input")

while True:
    try:
        rate_str = input("Enter Rate: ")
        rate = float(rate_str)
        break
    except:
        print("Error, please enter numeric input")

if hours >= 40:
    total = (rate * 40) + (hours - 40) * (rate * 1.5)
else:
    total = rate * hours

print("Pay: ", total)