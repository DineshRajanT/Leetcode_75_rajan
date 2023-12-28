class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        # for binary number u should 2 to get last position by %2 and //2 to shift bits to right>>
        # for other numbers it is 10 , just in binary it is 2

        while n:
            last = n % 2
            if last==1:
                res+=1
            n = n>>1 # shift right whihc is similar to (n = n //2) getting rid of the last bit

        return res


        # BIT MANIPULATION: 
        
        # res = 0
        # # (n - 1) removes the right most 1's everytime we subtract a binary number with 1
        # while n:
        #     n = n & (n-1)
        #     res+=1
        # return res
        