# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Inorder traversal mainted with a count when the node becomes visited(when poped from stack)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to keep track of nodes during traversal
        stack = []
        # Variable to count the number of visited nodes
        countNode = 0
        # Start from the root of the tree
        curr = root

        # Continue the loop as long as there are nodes to process or the stack is not empty
        while curr or stack:
            # Traverse to the leftmost node and push each node onto the stack
            while curr:
                stack.append(curr)
                curr = curr.left # keep going the left most node

            # Pop the top node from the stack (current node in the leftmost subtree)
            curr = stack.pop()
            # Increment the count of visited nodes
            countNode += 1

            # Check if the current node is the kth smallest
            if countNode == k:
                return curr.val

            # Move to the right subtree to continue the inorder traversal
            curr = curr.right

        # Return -1 if kth smallest element is not found (out of bounds)
        return -1






'''        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        countNode = [0]  # Using a list to mimic a mutable variable

        def inOrder(root, k):
            # Base case: if the root is None, return -1 (or any invalid value)
            if root is not None:
                # Traverse the left subtree
                left_result = inOrder(root.left, k)

                # If kth smallest is found in the left subtree, return it
                if left_result != -1:
                    return left_result

                # Update the count and check if the current node is the kth smallest
                countNode[0] += 1
                if countNode[0] == k:
                    return root.val

                # Traverse the right subtree
                right_result = inOrder(root.right, k)

                # Return the result from the right subtree
                return right_result
            else:
                return -1

        # Call the inOrder function and return its result
        return inOrder(root, k)
'''