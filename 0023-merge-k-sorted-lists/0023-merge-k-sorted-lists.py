from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Check if the input list is empty
        if not lists or len(lists) == 0:
            return None

        # Iterate until there is only one merged list
        while len(lists) > 1:
            mergedLL = []
            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                l1  = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                newMergedList = self.mergeTwoLists(l1, l2)
                mergedLL.append(newMergedList)
            lists = mergedLL

        # Return the final merged list
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # Check if either list is empty
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # Initialize a dummy node for the merged list
        dummyNode = ListNode()
        tail = dummyNode

        # Merge the two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append any remaining elements from both lists
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the merged list starting from the next of the dummy node
        return dummyNode.next
    """
    Time Complexity:
        - mergeKLists: O(N log k), where N is the total number of nodes in all lists, and k is the number of lists.
                       The dominant factor is the merging step, which takes O(N log k) time.
        - mergeTwoLists: O(N), where N is the total number of nodes in the two input lists.

    Space Complexity:
        - mergeKLists: O(1), as we are using constant extra space for variables, and the merging is done in-place
                       without using additional data structures.
        - mergeTwoLists: O(1), as we are using constant extra space for variables, and the merging is done in-place
                         without using additional data structures.
    """
