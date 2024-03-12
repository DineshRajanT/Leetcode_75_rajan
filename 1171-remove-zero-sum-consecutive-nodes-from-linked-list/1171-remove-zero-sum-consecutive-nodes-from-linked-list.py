# Define a class for a ListNode, which represents a node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define a class Solution, which contains the method removeZeroSumSublists
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node and set its next pointer to the head of the input linked list
        dummy = ListNode(0)
        dummy.next = head
        # Initialize a variable to keep track of the prefix sum
        prefix_sum = 0
        # Create a dictionary to store the prefix sums and their corresponding nodes
        prefix_sum_map = {}
        
        # Iterate through the linked list to calculate prefix sums and store them in the dictionary
        current = dummy
        
        while current:
            prefix_sum += current.val
            prefix_sum_map[prefix_sum] = current
            current = current.next
        

        # Reset the current node to the dummy node and prefix sum to 0
        current = dummy
        prefix_sum = 0
        
        # Iterate through the linked list again to remove zero-sum sublists
        while current:
            prefix_sum += current.val
            # Check if the current prefix sum exists in the prefix_sum_map
            if prefix_sum in prefix_sum_map:
                # If it exists, update the next pointer of the current node to skip the zero-sum sublist
                current.next = prefix_sum_map[prefix_sum].next
            # Move to the next node in the linked list
            current = current.next
        
        # Return the modified linked list (excluding zero-sum sublists)
        return dummy.next
