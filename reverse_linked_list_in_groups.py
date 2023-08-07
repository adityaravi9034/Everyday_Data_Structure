"""You are given a linked list that contains integers. Your task is to reverse the linked list in groups of a given size k.
If the number of nodes in the last group is less than k, you should leave those nodes as they are.

Write a function reverse_linked_list_in_groups(head, k) that takes the head of the linked list and the group size k as inputs and 
returns the head of the reversed linked list.

The ListNode class for representing the linked list is provided below:
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
Example:
Consider the following linked list and k = 3:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> None

"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def reverse_linked_list_in_groups(head, k):
    def reverse_group(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while head:
        count = 0
        group_start = head
        while head and count < k:
            head = head.next
            count += 1

        if count == k:
            group_end = head
            prev_group_end.next = reverse_group(group_start, group_end)
            prev_group_end = group_start

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
values = [1, 2, 3, 4, 5, 6]
k = 3
head = create_linked_list(values)
reversed_head = reverse_linked_list_in_groups(head, k)
print_linked_list(reversed_head)  # Output: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> None
