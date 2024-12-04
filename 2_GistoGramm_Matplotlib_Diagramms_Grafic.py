import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20, 3, 4, 5]


plt.hist(x, bins=4)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')

plt.show()