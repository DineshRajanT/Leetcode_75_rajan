class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSub = ""

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check palindromes with the current character as the center (odd length)
            s1 = self.checkPalindrome(s, i, i)
            
            # Check palindromes with the current and next characters as the center (even length)
            s2 = self.checkPalindrome(s, i, i+1)
            
            # Update the longest palindrome substring using the maximum length
            longestSub = max(s1, s2, longestSub, key=len)

        return longestSub

    def checkPalindrome(self, s, l, r):
        tempSub = ""

        # Expand the palindrome by comparing characters at positions 'l' and 'r'
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Update the current palindrome substring
            currSub = s[l:r+1]
            
            # Update the temporary palindrome substring using the maximum length
            tempSub = max(tempSub, currSub, key=len)
            
            # Move the pointers away from the center
            l -= 1
            r += 1

        return tempSub

# Time Complexity: O(n^2) - Two nested loops, each traversing the string with at most n characters
# Space Complexity: O(1) - Constant space is used for variables (`tempSub`, `l`, and `r`)
