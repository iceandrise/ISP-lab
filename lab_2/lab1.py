import numpy as np 

print("Input count of rows and columns:")
n,m = [int(i) for i in input().split()]
print("Input the first array:")
arr1 = [[int(input()) for j in range(m)] for i in range(n)]
print("Input the second array:")
arr2 = [[int(input()) for j in range(m)] for i in range(n)]
a = np.array(arr1)
b = np.array(arr2)
res=a+b
   
print("Result array:")
print(res)