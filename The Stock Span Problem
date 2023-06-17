"""The stock span problem is a financial problem where we have a series of N daily price quotes for a stock and we need to calculate the span of the 
stock’s price for all N days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than its price on the given day. 

Examples:

Input: N = 7, price[] = [100 80 60 70 60 75 85]
Output: 1 1 1 2 1 4 6
Explanation: Traversing the given input span for 100 will be 1, 80 is smaller than 100 so the span is 1,
60 is smaller than 80 so the span is 1, 70 is greater than 60 so the span is 2 and so on. Hence the output will be 1 1 1 2 1 4 6.

Input: N = 6, price[] = [10 4 5 90 120 80]
Output:1 1 2 4 5 1
Explanation: Traversing the given input span for 10 will be 1, 4 is smaller than 10 so the span will be 1,
5 is greater than 4 so the span will be 2 and so on. Hence, the output will be 1 1 2 4 5 1."""


def calculateSpan(price, n, S):
 
    # Span value of first day is always 1
    S[0] = 1
 
    # Calculate span value of remaining days by linearly
    # checking previous days
    for i in range(1, n, 1):
        S[i] = 1   # Initialize span value
 
        # Traverse left while the next element on left is
        # smaller than price[i]
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1
 
# A utility function to print elements of array
 
 
def printArray(arr, n):
 
    for i in range(n):
        print(arr[i], end=" ")
 
 
# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n
 
# Fill the span values in list S[]
calculateSpan(price, n, S)
 
# print the calculated span values
printArray(S, n)
 
