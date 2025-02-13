import numpy as np

name="my name is:"
name2="suraj singh"
print(np.char.add(name,name2)) #add two string

print(np.char.upper(name)) #uppercase

print(np.char.lower(name2)) #lowercase

name3="hello india this is suraj" #split saparate word
print(np.char.split(name3))

print(np.char.replace(name3,"suraj","Reeni Ravan")) #replace name

