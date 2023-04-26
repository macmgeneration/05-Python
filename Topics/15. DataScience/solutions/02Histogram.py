import matplotlib.pyplot as plt

data = input("Enter a list of numbers separated by spaces: ").split()
data = [int(x) for x in data]

plt.hist(data)
plt.show()