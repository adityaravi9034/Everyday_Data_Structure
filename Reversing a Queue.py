"""Give an algorithm for reversing a queue Q. Only the following standard operations are allowed on queue. 

enqueue(x): Add an item x to the rear of the queue.
dequeue(): Remove an item from the front of the queue.
empty(): Checks if a queue is empty or not.
The task is to reverse the queue.

Examples: 

Input: Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Output: Q = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]


Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]"""

from collections import deque
 
# Function to reverse the queue
 
 
def reversequeue(queue):
    Stack = []
 
    while (queue):
        Stack.append(queue[0])
        queue.popleft()
 
    while (len(Stack) != 0):
        queue.append(Stack[-1])
        Stack.pop()
 
 
# Driver code
if __name__ == '__main__':
    queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
 
    reversequeue(queue)
    print(queue)
 
