# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at the middle node

        # Reverse the second half of the linked list
        curr = slow.next
        prev = None
        slow.next = None  # Disconnect the first half from the second half

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # 'prev' is the new head of the reversed linked list

        # Merge the first half and the reversed second half of the linked list
        first_head = head
        second_head = prev

        while second_head:
            # Save the next nodes to avoid losing the reference during the reordering
            first_tmp, second_tmp = first_head.next, second_head.next
            
            # Reorder nodes
            first_head.next = second_head
            second_head.next = first_tmp
            
            # Move to the next nodes for reordering
            first_head, second_head = first_tmp, second_tmp
