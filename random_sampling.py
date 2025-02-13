import numpy as np
import random as rd

print(np.random.random(10)) #give us random value 
print(np.random.random((3,3))) #3x3 array

print(np.random.randint(1,10)) #give us single value

print(np.random.randint(1,9,(4,4))) #give us random array 4x4 integer
print(np.random.randint(1,9,(2,4,4))) #give us 3d array

print(np.random.seed(10))       #3d array create
print(np.random.randint(1,9,(2,4,4)))




