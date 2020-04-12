import numpy as np
import pandas

original_array = [1, 2, 3]
a = np.array(original_array)
print(a, original_array)

print(type(a))

a = np.array([[1, 2], [3, 4]])
print(a)

a = np.array([[1, 2], [3, 4, 5]])
print(a)

a = np.arange(0, 100)
print(a)

a = np.zeros((5, 5))
print(a)

vector = np.linspace(0, 20, 5)
print(vector)

a = np.zeros(8)
print(a)
a = a.reshape((2, 2, 2))
print(a)
a = a.ravel()
print(a)

arr = np.arange(2, 20)
element = arr[6]
print(type(element))

arr = np.arange(20)
arr_slice = slice(1, 10, 2)
print(arr[arr_slice])
print(arr[2:9])
print(arr[2:])
print(arr[:9])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0:2, 0:2])
print(arr.shape)
print(arr.ndim)

np.savetxt("test.txt", arr)

arr = np.array([9, 4,8,4])
series = pandas.Series(arr)
print(series)

listx = [10, 20, 30, 40]
table = pandas.DataFrame(listx)
print(table)


