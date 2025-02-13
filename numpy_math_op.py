import numpy as np
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(1,10).reshape(3,3)
print(arr1)
print(arr2)

#Basic Mathematic Operation :-

#addition:
print(arr1+arr2) #normally
print(np.add(arr1,arr2))  #using numpy

#subtraction:
print(arr1-arr2) #normally
print(np.subtract(arr1,arr2))  #using numpy

#division:
print(arr1/arr2) #normally
print(np.divide(arr1,arr2))  #using numpy

#multiplication:
print(arr1*arr2) #normally
print(np.multiply(arr1,arr2))  #using numpy

#matrix:
print(arr1 @ arr2) #normally
print(arr1.dot(arr2))  #using numpy

#maximum value:
print(arr1.max()) 
print(arr2.max()) 

#maximum value index:
print(arr1.argmax()) 
print(arr2.argmax())

#maximum value in rows and colums:
print(arr1.max(axis=0))  #zero(0) represent colums
print(arr2.max(axis=1))  #one(1) represent rows

#minimum value:
print(arr1.min()) 
print(arr2.min())

#min value index:
print(arr1.argmin()) 
print(arr2.argmin())

#min. value in rows and colums:
print(arr1.min(axis=0))        #0=colums
print(arr2.min(axis=1))        #1=rows

#sum of arrays elements
print(np.sum(arr1))

#sum of arrays colums and rows 
print(np.sum(arr1,axis=0)) #colums=0/ sum of colums
print(np.sum(arr2,axis=1)) #rows=1/sum of rows 

#mean of matrix or arrays 
print(np.mean(arr1)) 
print(np.mean(arr2))


#squre root of elements:
print(np.sqrt(arr1))


#standard  division of elements
print(np.std(arr1))

#exponent of arrays:
print(np.exp(arr1))

#log of element in array:
print(np.log(arr1))

print(np.log10(arr1))


