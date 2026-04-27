# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Input validation
        if not head:
            return None

        # Init starting node.
        current_node = head
        # Save position of next node
        next_node = head.next
        # Init previous_node
        previous_node = None
        # Reverse initial pointer
        current_node.next = previous_node

        # We check if the next_node is not empty. Because if the .next value of a node is empty, 
        # it means we have reached the end, or tail, of the linked list.
        while next_node:
            
            # We have to move forward but still have to keep all necessary information to orient in one iteration.
            # We save the current_node in previous_node;
            previous_node = current_node
            # This leaves the current_node open to be overwritten with the next node;
            current_node = next_node
            # This in turn leaves the next_node open to be overwritten by the next_node
            next_node = next_node.next
            # All relevant information is kept in the right place, so therefore we can finally reverse the pointer of the current node, to the previous node.
            current_node.next = previous_node

        head = current_node

        return head


        