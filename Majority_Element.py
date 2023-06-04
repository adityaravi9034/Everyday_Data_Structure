"""Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 

Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is greater than the half of the size of the array size."""

def findMajority(arr, n):
 
    maxCount = 0
    index = -1  # sentinels
    for i in range(n):
 
        count = 1
        # here we compare the element in
        # ith position with i+1th position
        for j in range(i+1, n):
 
            if(arr[i] == arr[j]):
                count += 1
 
        # update maxCount if count of
        # current element is greater
        if(count > maxCount):
 
            maxCount = count
            index = i
 
    # if maxCount is greater than n/2
    # return the corresponding element
    if (maxCount > n//2):
        print(arr[index])
 
    else:
        print("No Majority Element")
 
 
# Driver code
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
 
    # Function calling
    findMajority(arr, n)
