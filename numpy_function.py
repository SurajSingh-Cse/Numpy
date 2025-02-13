import numpy as np

        #arange function
        #syntax=np.arange(start,ends,steps)

arr=np.arange(1,15)
arr2=np.arange(1,15,3)
print(arr)
print(arr2)

#linspace()
#sytax= np.linspace(start,ends,total_element between start and ends)

arr3=np.linspace(2,8,10)
print(arr3)


#reshape()
#it is used to covert 1d array to  multidimention array
#sytax=np.reshape(row,cols)

arr3=np.arange(1,13)
print(arr3)
print(arr3.reshape(2,6))
print(arr3.reshape(3,4))
print(arr3.reshape(4,3))



#ravel()
#it is used to convert multidimention array to 1-d array

arr4=np.array([[45,56,78,78,],[78,85,47,89],[45,12,32,65]])
print(arr4)          #2d array
print(arr4.ravel())     #1d array



#flatten()
#it is also convert multi dimention array to 1d array but we can give us parameter
print(arr4.flatten()) #convert one d array




#transpose() // it is used to multidimention array to convert 
#row to cols and cols to row.
#shortcut of transpose funtion "T"
ar=arr4.transpose()
print(ar)

#"T"
ar=arr4.T
print(ar)




