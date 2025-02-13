import numpy as np

arr=np.arange(1,101).reshape(10,10)

print(arr[5,4]) #find 55 number in array

print(arr[3,4]) #find 35 number in array

print(arr[0]) #find single row in array

print(arr[:,0]) #find single colums in array

print(arr[1:4, 1:4]) #find the particular row and cols

print(arr[:, 1:3]) #find particular colums