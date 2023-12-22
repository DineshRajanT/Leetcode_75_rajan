class Solution:
    def maxScore(self, s: str) -> int:
        globalCount = float("-inf")

        for i in range(len(s)):
            if s[0:i+1] and s[i+1:]:
                currCount = s[0:i+1].count('0') + s[i+1:].count('1')
                globalCount = max (globalCount, currCount)
        return globalCount

        