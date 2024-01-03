class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize a variable to store the result
        res = 0
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # Expand around the current character for odd-length palindromes
            res += self.countPalindromes(s, i, i)
            
            # Expand around the current and next characters for even-length palindromes
            res += self.countPalindromes(s, i, i+1)
        
        return res


    # keep the curr character and expanding in both directions, by keep the curr char as the middle char
    def countPalindromes(self, s, l, r):
        # Initialize a variable to store the count of palindromes
        tmp_res = 0
        
        # Expand the palindrome by comparing characters at positions 'l' and 'r'
        while l >= 0 and r < len(s) and s[l] == s[r]:
            tmp_res += 1
            l -= 1
            r += 1
        return tmp_res

# Time Complexity: O(n^2) - Two nested loops, each traversing the string with at most n characters
# Space Complexity: O(1) - Constant space is used for variables
