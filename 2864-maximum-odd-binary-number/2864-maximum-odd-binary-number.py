class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Convert the string to a list of characters
        s_list = list(s)

        # to make the binary string odd, you need to have one character to the right end
        # to maximize it try pushing all the remaining 1's to your left so it takes max contribution of 2**i

        n = len(s)
        l = 0
        r = n - 1

        # Iterate through the string from both ends
        while l <= r:
            # Move to the right if the current character is '1'
            if s_list[l] == '1':
                l += 1
            # Move to the left if the current character is '0'
            if s_list[r] == '0':
                r -= 1
            # Swap '0' from the left with '1' from the right to maximize the value
            if l <= r and s_list[l] == '0' and s_list[r] == '1':
                s_list[l], s_list[r] = s_list[r], s_list[l]

        # Make the rightmost swapped character '1' to ensure the number is odd
        s_list[l - 1], s_list[n - 1] = s_list[n - 1], s_list[l - 1]

        # Convert the list back to a string
        return ''.join(s_list)
