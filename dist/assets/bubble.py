import numpy as np
def bubble(arr1):
    for i in range(0,len(arr1)-1):
        for j in range(len(arr1)):
            if (arr1[j]>arr1[j+1]):
                temp=arr1[j]
                arr1[j]=arr1[j+1]
                arr1[j+1]=temp
    return arr1


arr1=[23,56,12,78]
print("original array", arr1)
print("sorted array", bubble(arr1))