"""You are given two queues, queue1 and queue2, each containing integer elements. Your task is to merge the two queues in a specific manner.
The merging process involves taking elements alternatively from queue1 and queue2, and creating a new queue with these elements. 
If one of the queues becomes empty before the other, the remaining elements of the non-empty queue should be added to the new queue.

Write a function merge_queues(queue1, queue2) that takes the two queues as input and returns the merged queue according to the specified merging process.

You are allowed to use the built-in list data structure to implement the queues.

queue1 = [1, 3, 5]
queue2 = [2, 4, 6, 8, 10]

merged_queue = merge_queues(queue1, queue2)
print(merged_queue)  # Output: [1, 2, 3, 4, 5, 6, 8, 10]


"""

def merge_queues(queue1, queue2):
    merged_queue = []
    while queue1 and queue2:
        merged_queue.append(queue1.pop(0))
        merged_queue.append(queue2.pop(0))
    merged_queue.extend(queue1)
    merged_queue.extend(queue2)
    return merged_queue

# Example usage:
queue1 = [1, 3, 5]
queue2 = [2, 4, 6, 8, 10]
merged_queue = merge_queues(queue1, queue2)
print(merged_queue)  # Output: [1, 2, 3, 4, 5, 6, 8, 10]
