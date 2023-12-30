class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize the result variable to store the reversed bits
        
        for i in range(32):  # Iterate 32 times assuming a 32-bit integer
            # Shift the current result to the left by 1 bit, and OR it with the rightmost bit of n
            res = (res << 1) | (n & 1)
            
            # Right shift n by 1 to get the next rightmost bit for the next iteration
            n >>= 1

        return res  # Return the final result with reversed bits

'''
** Initialization: 
res is initialized to 0. This variable will store the reversed bits.

** Looping 32 times: 
The loop runs 32 times since we assume a 32-bit integer. In each iteration:

** Bitwise Left Shift (res << 1): 
The current res is shifted to the left by 1 bit. This makes room for the next bit to be added.

** Bitwise AND (n & 1): 
This extracts the rightmost bit of n.

** Bitwise OR (|): 
The shifted res is combined with the rightmost bit of n using OR, effectively adding the rightmost bit to the reversed result.

** Right Shift (n >>= 1): 
After extracting the rightmost bit of n, it is right-shifted by 1 position, so the next iteration will process the next bit.

** turn: The final reversed result is returned after 32 iterations.
'''