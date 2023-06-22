"""Implementing a stack data structure using an array in Python.

push(item): Adds an item to the top of the stack.
pop(): Removes and returns the item from the top of the stack.
peek(): Returns the item from the top of the stack without removing it.
is_empty(): Returns a boolean indicating whether the stack is empty.
size(): Returns the number of items in the stack."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.size())      # Output: 3
print(stack.peek())      # Output: 15
print(stack.pop())       # Output: 15
print(stack.is_empty())  # Output: False

