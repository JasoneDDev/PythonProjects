import numpy as np
x = np.ones((5,5))
print("Normal array: \n", x)

print('\n')

x[1:-1, 1:-1] = 0

print(x)

x = [10, 15, 22, 24]
x = np.append(x, [[30,40,50], [60,70,2]])
print('\n',x)

x = np.sort(x)
print(x)