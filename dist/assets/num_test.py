import numpy as n
def sel_sort(arr1):
    n=len(arr1)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr1[j]<arr1[mini]:
                mini=j
                arr1[j],arr1[mini]=arr1[minip],arr1[j]

arr1=[23,56,12,78]
print("original array", arr1)
print("sorted array", sel_sort(arr1))
