"""You are tasked with implementing a queue that supports an additional operation called get_max(). The get_max() operation returns the maximum element currently present in the queue. You need to design a data structure and implement the necessary functions to support this queue.

Write a class MaxQueue that represents the queue with the get_max() operation. The class should include the following methods:

enqueue(value): Adds the given value to the rear of the queue.
dequeue(): Removes and returns the front element from the queue.
get_max(): Returns the maximum element currently present in the queue.
You can assume that all elements in the queue are integers.

You are allowed to use the built-in list data structure to implement the queue.

max_queue = MaxQueue()
max_queue.enqueue(5)
max_queue.enqueue(10)
max_queue.enqueue(3)

print(max_queue.get_max())  # Output: 10

max_queue.dequeue()
print(max_queue.get_max())  # Output: 10

max_queue.enqueue(15)
print(max_queue.get_max())  # Output: 15


"""

class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_values = []

    def enqueue(self, value):
        self.queue.append(value)

        if not self.max_values or value >= self.max_values[-1]:
            self.max_values.append(value)

    def dequeue(self):
        if not self.queue:
            return None

        value = self.queue.pop(0)

        if value == self.max_values[0]:
            self.max_values.pop(0)

        return value

    def get_max(self):
        return self.max_values[0] if self.max_values else None

# Example usage:
max_queue = MaxQueue()
max_queue.enqueue(5)
max_queue.enqueue(10)
max_queue.enqueue(3)

print(max_queue.get_max())  # Output: 10

max_queue.dequeue()
print(max_queue.get_max())  # Output: 10

max_queue.enqueue(15)
print(max_queue.get_max())  # Output: 15
