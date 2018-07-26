import numpy as np
x = np.array([1,2,3], dtype=np.float64)

first_array = np.array([0,10,20,30,40,50,60])
second_array = np.array([10,40,50])
print('\n find common: ', np.in1d(first_array, second_array))

print('\n intersect: ', np.intersect1d(first_array, second_array))

a = np.array([1,3])
b= np.array([2,4])

print(np.dot(a, b))