# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##### ITERATIVE SOLUTION.......

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         prevNode = None
#         currNode = head
#         while currNode is not None:
#             nextNode = currNode.next
#             currNode.next = prevNode
#             prevNode = currNode
#             currNode = nextNode
#         return prevNode # New head
      
#### RECURSIVE SOLUTION.......
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        # First change the link b/w curr and prev and then call the same for subsequent nodes.
        def reverse(curr, prev):
            if curr is None:
                return prev
            next = curr.next
            curr.next = prev
            return reverse(next, curr)
            
        return reverse(curr, prev)
            
        