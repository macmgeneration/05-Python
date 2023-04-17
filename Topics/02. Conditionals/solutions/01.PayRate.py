hours_str = input("Enter Hours: ")
rate_str = input("Enter Rate: ")

hours = float(hours_str)
rate = float(rate_str)

if hours >= 40:
    total = (rate * 40) + (hours - 40) * (rate * 1.5)
else:
    total = rate * hours

print("Pay: ", total)