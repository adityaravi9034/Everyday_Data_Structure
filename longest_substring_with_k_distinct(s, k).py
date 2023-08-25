"""You are given a string s containing only lowercase letters.
Your task is to find the longest substring in s that contains at most k distinct characters.

Write a function longest_substring_with_k_distinct(s, k) that takes the string s and the integer k as inputs
and returns the length of the longest substring that meets the criteria.
Example 
s = "eceba"
k = 2

length = longest_substring_with_k_distinct(s, k)
print(length)  # Output: 3

Explanation: In the given example, the longest substring with at most 2 distinct characters is "ece".

"""
def longest_substring_with_k_distinct(s, k):
    max_length = 0
    char_count = {}
    left = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "eceba"
k = 2

length = longest_substring_with_k_distinct(s, k)
print(length)  # Output: 3
