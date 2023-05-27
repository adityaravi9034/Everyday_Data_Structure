"""Given a pair-sum array and size of the original array (n), construct the original array.
A pair-sum array for an array is the array that contains sum of all pairs in ordered form. For example pair-sum array for arr[] = {6, 8, 3, 4} is {14, 9, 10, 11, 12, 7}.
In general, pair-sum array for arr[0..n-1] is {arr[0]+arr[1], arr[0]+arr[2], ……., arr[1]+arr[2], arr[1]+arr[3], ……., arr[2]+arr[3], arr[2]+arr[4], …., arr[n-2]+arr[n-1}.
“Given a pair-sum array, construct the original array.”

"""

def constructArr(arr,pair,n):
    arr [0] = (pair[0]+pair[1]-pair[n-1])//2
    for i in range(1,n):
        arr[i] = pair[i-1]-arr[0]
 
# Driver code
if __name__=='__main__':
    pair = [15, 13, 11, 10, 12, 10, 9, 8, 7, 5]
    n =5
    arr = [0]*n
    constructArr(arr,pair,n)
    for i in range(n):
        print(arr[i],end =" ")
 
