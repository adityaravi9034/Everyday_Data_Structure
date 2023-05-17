"""Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 

Example:

Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the 
array is 35 and the second 
largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second largest does not exist.
Explanation: Largest element of the array 
is 10 there is no second largest element"""


from collections import defaultdict

def second_largest(n, vec):
	# size of array should be greater than 1
	if n < 2:
		print("Invalid Input")
		return

	count = defaultdict(int)
	for i in range(n):
		count[vec[i]] += 1

	# Checking if count size is equal to 1 it
	# means only largest element exist there is no second
	# largest element
	if len(count) == 1:
		print("No Second largest element exist")
		return

	# sort the dictionary by key in descending order
	count_sorted = sorted(count.items(), key=lambda x: x[0], reverse=True)
	second_largest = None
	for i, (key, value) in enumerate(count_sorted):
		if i == 1:
			second_largest = key
			break

	if second_largest is not None:
		print("The second largest element is:", second_largest)

vec = [12, 35, 1, 10, 34, 1]
second_largest(len(vec), vec)

