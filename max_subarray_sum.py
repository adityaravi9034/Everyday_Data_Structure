"""You are given an array of integers nums and an integer k. Your task is to find the maximum sum of a subarray of size k.

Write a function max_subarray_sum(nums, k) that takes the array of integers nums and the integer k as inputs and returns the maximum sum of any subarray of size k.

Example:
nums = [10, 5, 2, 7, 8, 7]
k = 3

max_sum = max_subarray_sum(nums, k)
print(max_sum)  # Output: 18
"""
def max_subarray_sum(nums, k):
    max_sum = float('-inf')
    current_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [10, 5, 2, 7, 8, 7]
k = 3

max_sum = max_subarray_sum(nums, k)
print(max_sum)  # Output: 18
