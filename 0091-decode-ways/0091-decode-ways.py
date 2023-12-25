class Solution:
    def numDecodings(self, s: str) -> int:
        # Handle edge case: if the first digit is '0', there's no valid decoding
        if s[0] == '0':
            return 0
        
        # Initialize dp array to store the number of ways to decode at each position
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # There is one way to decode an empty string
        
        for i in range(1, len(s) + 1):
            ### Below If else code portion is for Single digit position checks:

            # Check if the current digit is '0'
            if s[i - 1] == '0':
                # If the current digit is '0', it cannot be decoded by itself,
                # so the number of ways to decode at this position is 0.
                dp[i] = 0
            else:
                # If the current digit is not '0', it can be decoded by itself,
                # so the number of ways to decode at this position is the same as
                # the number of ways to decode at the previous position.
                dp[i] = dp[i - 1]
            
            ### Below Code portion is for Double digit position checks:
            
            # Check if the current and previous digit form a valid two-digit number
            # check from second index position and look back two indices.....
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                # If valid, add the number of ways to decode at two positions back
                dp[i] += dp[i - 2]
        print(dp)
        return dp[-1]


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s) : 1}
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i+1]

#             if i+1 < len(s) and (s[i] == "1" or
#                                  s[i] == "2" and s[i+1] in "0123456") :
#                 dp[i] += dp[i+2]

#         print(dp)
#         return dp[0]

        