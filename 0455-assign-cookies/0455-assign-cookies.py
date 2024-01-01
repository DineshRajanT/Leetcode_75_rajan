class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0 or len(g) == 0:
            return 0

        g.sort()
        s.sort()

        content_children = 0
        i, j = 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                # Child can be content with the current cookie
                content_children += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie

        return content_children
