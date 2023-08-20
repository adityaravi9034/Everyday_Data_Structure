"""Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side). 

Examples: 


Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles 
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. 
Note that {3, 4, 7} is not a possible triangle.  

Input: arr= {10, 21, 22, 100, 101, 200, 300}.
Output: 6
Explanation: There can be 6 possible triangles:
{10, 21, 22}, {21, 100, 101}, {22, 100, 101}, 
{10, 100, 101}, {100, 101, 200} and {101, 200, 300}"""

def findNumberOfTriangles(arr, n):
 
    # Count of triangles
    count = 0
 
    # The three loops select three
    # different values from array
    for i in range(n):
        for j in range(i + 1, n):
 
            # The innermost loop checks for
            # the triangle property
            for k in range(j + 1, n):
 
                # Sum of two sides is greater
                # than the third
                if (arr[i] + arr[j] > arr[k] and
                    arr[i] + arr[k] > arr[j] and
                        arr[k] + arr[j] > arr[i]):
                    count += 1
    return count
 
 
# Driver code
if __name__ == "__main__":
    arr = [10, 21, 22, 100, 101, 200, 300]
    size = len(arr)
 
    # Function call
    print("Total number of triangles possible is",
          findNumberOfTriangles(arr, size))
