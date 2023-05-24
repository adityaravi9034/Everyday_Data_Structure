"""Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according to given index array. It is not allowed to given array arr’s length.

Example: 

Input:  arr[]   = [10, 11, 12];
            index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
           index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
          index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
          index[] = [0,  1,  2,  3,   4]"""
          
          
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
 
# result = (original + update%z*z) ..
def rearrange(arr, index):
    z = findMax(arr) + 1
    for i in range(len(arr)):
        arr[index[i]] = arr[index[i]] % z + arr[i] % z * z
 
    for i in range(len(arr)):
        arr[i] = arr[i]//z
 
 
def findMax(arr):
    Max = float("-inf")
    for i in range(len(arr)):
        if(Max < arr[i]):
            Max = arr[i]
 
    return Max
 
arr = [23, 12, 20, 10, 23]
index = [4, 0, 1, 2, 3]
 
rearrange(arr, index)
printArray(arr)
