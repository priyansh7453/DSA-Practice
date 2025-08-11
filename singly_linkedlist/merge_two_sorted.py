# merge of two sorted linked lists
from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    # Initialize the merged list
    if head1.data < head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next
    
    current = merged_head
    
    # Merge the two lists
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    
    # Attach the remaining elements
    if head1:
        current.next = head1
    elif head2:
        current.next = head2
    
    return merged_head

if __name__ == "__main__":
    # Create two sorted linked lists:
    # List 1: 10 -> 20 -> 30
    head1 = Node(10)
    head1.next = Node(20)
    head1.next.next = Node(30)
    
    # List 2: 15 -> 25 -> 35
    head2 = Node(15)
    head2.next = Node(25)
    head2.next.next = Node(35)
    
    print("List 1:")
    traversal(head1)
    
    print("List 2:")
    traversal(head2)
    
    merged_head = merge_sorted_lists(head1, head2)
    
    print("Merged List:")
    traversal(merged_head)  # Should print the merged sorted list
# This code merges two sorted linked lists into one sorted linked list.
# The merged list will maintain the sorted order of elements.

