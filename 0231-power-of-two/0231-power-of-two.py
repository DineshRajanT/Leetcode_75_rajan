class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if 0 == n - (n & (-n)):
            return True
        return False
        
        # T : O(1) 
        # S : O(1)
        # (-n) ==> n's two complement (i.e) flipping the bits and adding one to it
        # (n & (-n) == > gives the last set bit
        # and subtractig the last set bit, the n should become zero, then it is power of two
        #Fenwick tree