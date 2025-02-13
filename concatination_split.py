import numpy as np

ar1=np.arange(1,17).reshape(4,4)
ar2=np.arange(17,33).reshape(4,4)

print(ar1)
print(ar2)

#concatination by colums
print(np.concatenate((ar1,ar2)))
#concatination by colums
print(np.vstack((ar1,ar2)))

#concatination by rows
print(np.concatenate((ar1,ar2),axis=1))
#concatination by rows
print(np.hstack((ar1,ar2)))

 
 #split funtion:
print(np.split(ar1, 2))

#split array by colums
print(np.split(ar1,2, axis=1))
 