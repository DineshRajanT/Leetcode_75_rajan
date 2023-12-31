# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # move first pointer N nodes first in a initila loop and then 
        # initilaize one more pointer as second from head , 
        # move them parallely one step and when first reaches the end the second will be at the desired position.
        if head == None:
            return

        # Create a dummy node before the head to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers (first and second) to the dummy node
        first = dummy
        second = dummy

        # Move first pointer N nodes ahead
        for i in range(n + 1): # here is n+1 because we need to have hold of the prev node of the node to delete.
            if first is None:
                return None  # If N is greater than the length of the linked list

            first = first.next

        # Move first and second pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Return the modified linked list
        return dummy.next