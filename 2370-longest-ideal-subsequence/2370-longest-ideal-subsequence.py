class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i][j] represents the length of the longest ideal string ending at index i with difference j
        dp = [[0] * 26 for _ in range(n)]
        
        # Iterate over each character in the string
        for i in range(n):
            # Iterate over each possible difference value (0 to 25) between characters
            for j in range(26):
                # Base case: if we are at the first character
                if i == 0:
                    # Set dp[i][j] to 1 if the first character matches the current character index 'j'
                    dp[i][j] = 1 if ord(s[i]) - ord('a') == j else 0
                else:
                    # Update dp[i][j] with the maximum value from the previous character
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    # Check if the current character matches the current character index 'j'
                    if ord(s[i]) - ord('a') == j:
                        # Iterate over all possible previous character indices 'prev'
                        for prev in range(26):
                            # Check if the absolute difference between 'prev' and 'j' is within 'k'
                            if abs(prev - j) <= k:
                                # Update dp[i][j] with the maximum value from the previous character index 'prev'
                                dp[i][j] = max(dp[i][j], dp[i - 1][prev] + 1)
        
        # Return the maximum value among all elements in dp
        return max(max(row) for row in dp)
