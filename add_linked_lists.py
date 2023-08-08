"""You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order, and each of their nodes contains a single digit. Your task is to add the two numbers and return the sum as a linked list.

Write a function add_linked_lists(l1, l2) that takes the heads of the two linked lists as inputs and returns the head of the resulting linked list representing the sum.

The ListNode class for representing the linked list is provided below:

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
Consider the following linked lists:

l1: 2 -> 4 -> 3 -> None
l2: 5 -> 6 -> 4 -> None
The expected output for this example is:

result: 7 -> 0 -> 8 -> None
Explanation: The sum of 342 and 465 is 807.

"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def add_linked_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
            
    return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
values1 = [2, 4, 3]
values2 = [5, 6, 4]
l1 = create_linked_list(values1)
l2 = create_linked_list(values2)
result = add_linked_lists(l1, l2)
print_linked_list(result)  # Output: 7 -> 0 -> 8 -> None
