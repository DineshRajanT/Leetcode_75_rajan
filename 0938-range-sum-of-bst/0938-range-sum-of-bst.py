# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.sumVal = 0
        
        
        def calcSum(Node):

            if Node is None:
                return 0

            if Node.val>=low and Node.val<=high:
                self.sumVal += Node.val

            if Node.left is not None:
                calcSum(Node.left)

            if Node.right is not None:
                calcSum(Node.right)
            return self.sumVal

        return calcSum(root)
            

