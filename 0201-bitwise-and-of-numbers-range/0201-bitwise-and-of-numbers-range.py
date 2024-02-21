class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Loop until right is greater than left
        while right > left:
            # Bitwise AND operation with (right - 1)
            # This operation turns off the rightmost set bit in 'right'
            right = right & (right - 1)
            
        # Return the final 'right' value after the loop
        return right
