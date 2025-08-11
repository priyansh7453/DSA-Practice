# Detect and remove loop in a singly linked list
from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def detect_and_remove_loop(head):
    if head is None:
        return None
    slow = head
    fast = head
    loop_found = False
    # Step 1: Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_found = True
            break
    if not loop_found:
        return head  # No loop
    # Step 2: Find the start node of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    # Step 3: Remove the loop
    # Traverse to the last node and set next to None
    temp = fast
    while temp.next != fast:
        temp = temp.next
    temp.next = None
    return head

if __name__ == "__main__":
    # Create a hard-coded linked list with a loop:
    # 10 -> 20 -> 30 -> 88 -> 550 ->760
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    
    # Creating a loop for testing
    # head.next.next.next.next.next.next = head.next  # Loop back to node with data 20
    
    print("Before removing loop:")
    traversal(head)  # This will cause an infinite loop if not handled
    
    head = detect_and_remove_loop(head)
    
    print("After removing loop:")
    traversal(head)  # Should print the list without any loops  
    