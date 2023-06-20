"""Given K sorted arrays of size N each, merge them and print the sorted output.

Examples:

Input: K = 3, N = 4, arr = { {1, 3, 5, 7}, {2, 4, 6, 8}, {0, 9, 10, 11}}
Output: 0 1 2 3 4 5 6 7 8 9 10 11 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. 

Input: k = 4, n = 4, arr = { {1, 5, 6, 8}, {2, 4, 10, 12}, {3, 7, 9, 11}, {13, 14, 15, 16}} 
Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. """

def mergeKArrays(arr, a, output):
    c = 0
  
    # traverse the matrix
    for i in range(a):
        for j in range(4):
            output = arr[i][j]
            c += 1
  
    # sort the array
    output.sort()
  
# A utility function to print array elements
  
  
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
  
  
# Driver's code
if __name__ == '__main__':
    arr = [[2, 6, 12, 34], [1, 9, 20, 1000], [23, 34, 90, 2000]]
    K = 4
    N = 3
    output = [0 for i in range(N * K)]
  
    # Function call
    mergeKArrays(arr, N, output)
  
    print("Merged array is ")
    printArray(output, N * K)
