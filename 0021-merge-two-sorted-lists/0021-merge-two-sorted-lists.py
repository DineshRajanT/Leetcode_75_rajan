# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        curr1 = list1
        curr2 = list2
        head = tail = None

        if curr1 is None:
            return curr2
        if curr2 is None:
            return curr1

        # Fixing head whichever is small and move the tail
        if curr1.val < curr2.val:
            head = tail = curr1
            curr1 = curr1.next
        else:
            head = tail = curr2
            curr2 = curr2.next

        # compare which is small and attach the small val to the next of tail 
        # and move tail to curr(keep to hold of it) and increment the curr
        while (curr1 != None and curr2 != None):

            if curr1.val < curr2.val:
                tail.next = curr1 
                tail = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = curr2
                curr2 = curr2.next

        # If we come out of the loop by any one of the curr1/curr2 getting None, 
        # then attach the remaining portion to the end of the tail
        if curr1 == None:
            tail.next = curr2
        else:
            tail.next = curr1

        return head
            


        