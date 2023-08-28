"""You are given a list of integers, and you want to calculate the average of each subarray of size k. 
Your task is to write a function that calculates and returns the list of averages.

Write a function subarray_averages(nums, k) that takes the list of integers nums and the integer k as inputs and 
returns a list of averages of all subarrays of size k.

Example
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 4

averages = subarray_averages(nums, k)
print(averages)  # Output: [3.0, 2.5, 1.5, 3.5, 2.5, 3.5, 3.5]

In the given example, the subarrays of size 4 are [1, 3, 2, 6], [3, 2, 6, -1], [2, 6, -1, 4], [6, -1, 4, 1], [4, 1, 8, 2].
The averages of these subarrays are [3.0, 2.5, 1.5, 3.5, 2.5, 3.5].
"""
def subarray_averages(nums, k):
    averages = []
    window_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        averages.append(window_sum / k)

    return averages

# Example usage:
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 4

averages = subarray_averages(nums, k)
print(averages)  # Output: [3.0, 2.5, 1.5, 3.5, 2.5, 3.5, 3.5]
