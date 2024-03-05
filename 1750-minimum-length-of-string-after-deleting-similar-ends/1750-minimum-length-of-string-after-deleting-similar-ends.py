class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize left and right pointers
        l = 0
        r = len(s) - 1

        # Continue moving the pointers inward as long as characters match
        while l < r and s[l] == s[r]:
            # Move the left pointer inward while consecutive characters match
            while l < r and s[l] == s[l + 1]:
                l += 1
            # Move the right pointer inward while consecutive characters match
            while l < r and s[r] == s[r - 1]:
                r -= 1
            # Move both pointers inward
            l += 1
            r -= 1

        # Calculate the remaining length of the string after applying operations
        # max(0, r - l + 1) ensures the length is non-negative
        return max(0, r - l + 1)
