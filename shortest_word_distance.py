"""You are given a list of words and two words, word1 and word2. Your task is to find the shortest distance between word1 and word2 in the list of words.

Write a function shortest_word_distance(words, word1, word2) that takes the list of words and the two words word1 and word2 
as inputs and returns the shortest distance between them.

Example

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

distance = shortest_word_distance(words, word1, word2)
print(distance)  # Output: 3
Explanation: In the given example, the words "coding" and "practice" are separated by three words."""

def shortest_word_distance(words, word1, word2):
    index1, index2 = None, None
    min_distance = float('inf')

    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i

        if index1 is not None and index2 is not None:
            min_distance = min(min_distance, abs(index1 - index2))

    return min_distance

# Example usage:
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

distance = shortest_word_distance(words, word1, word2)
print(distance)  # Output: 3
