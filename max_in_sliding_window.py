"""You are given a list of integers and an integer k. Your task is to find the maximum element for each contiguous subarray of 
size k and return the list of these maximums.

Write a function max_in_sliding_window(nums, k) that takes the list of integers nums and the integer k as inputs and returns a list of
the maximum elements for each subarray of size k.

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

Example:

result = max_in_sliding_window(nums, k)
print(result)  # Output: [3, 3, 5, 5, 6, 7]
In the given example, the maximum elements for each subarray of size 3 are [3, 3, 5, 5, 6, 7]."""

def max_in_sliding_window(nums, k):
    max_values = []
    deque = []

    for i, num in enumerate(nums):
        while deque and num > nums[deque[-1]]:
            deque.pop()
        deque.append(i)

        if i - deque[0] >= k:
            deque.pop(0)

        if i >= k - 1:
            max_values.append(nums[deque[0]])

    return max_values

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_in_sliding_window(nums, k)
print(result)  # Output: [3, 3, 5, 5, 6, 7]
