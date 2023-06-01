"""Given a list of distinct unsorted integers, find the pair of elements that have the smallest absolute difference between them? If there are multiple pairs, find them all.

Examples: 

Input : arr[] = {10, 50, 12, 100}
Output : (10, 12)
The closest elements are 10 and 12

Input : arr[] = {5, 4, 3, 2}
Output : (2, 3), (3, 4), (4, 5)"""

def printMinDiffPairs(arr , n):
    if n <= 1: return
 
    # Sort array elements
    arr.sort()
     
    # Compare differences of adjacent
    # pairs to find the minimum difference.
    minDiff = arr[1] - arr[0]
    for i in range(2 , n):
        minDiff = min(minDiff, arr[i] - arr[i-1])
 
    # Traverse array again and print all
    # pairs with difference as minDiff.
    for i in range(1 , n):
        if (arr[i] - arr[i-1]) == minDiff:
            print( "(" + str(arr[i-1]) + ", "
                 + str(arr[i]) + "), ", end = '')
 

arr = [5, 3, 2, 4, 1]
n = len(arr)
printMinDiffPairs(arr , n)
