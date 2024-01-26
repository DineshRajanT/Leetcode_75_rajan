# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True 

        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))

        return False

    



        '''

        def preOrderTraversal(node, sequence):
            if node is None:
                sequence.append(-1)
            else:
                sequence.append(node.val)
                preOrderTraversal(node.left, sequence)
                preOrderTraversal(node.right, sequence)
                return sequence

        seq1 = preOrderTraversal(p, [])
        seq2 = preOrderTraversal(q, [])
        print(seq1)
        print(seq2)
        # check if the the preorder traversal is same for both the trees
        return seq1 == seq2

        '''
            

        