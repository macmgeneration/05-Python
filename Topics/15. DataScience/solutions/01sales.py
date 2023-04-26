import matplotlib.pyplot as plt

years = []
sales = []

n_years = int(input("How many years do you want to enter? "))

for i in range(n_years):
    year = int(input(f"Enter the year {i+1}: "))
    years.append(year)
    sale = float(input(f"Enter the sales for {year}: "))
    sales.append(sale)

plt.plot(years, sales)
plt.title("Sales per year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()