import numpy as np
# create one's array 
#by default one's array is float
arr_2d=np.ones((5,8))
print(arr_2d)
print(type(arr_2d))
print(arr_2d.ndim)


#change the datatype of one's array 
arr_2d=np.ones((5,8),dtype=bool)
print(arr_2d)

#create zero's array
arr_2d=np.zeros((4,6))
print(arr_2d)

