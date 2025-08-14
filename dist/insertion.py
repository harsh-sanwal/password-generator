import numpy as np

def insertion(arr1):
    n=len(arr1)
    for i in range(1,n):
        key=arr1[i]
        j=i-1
        while j>=0 and key<arr1[j]:
            arr1[j+1]=arr1[j]
            j-=1
        arr1[j+1]=key
        


arr=np.array([56,76,23,64,98])
insertion(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")