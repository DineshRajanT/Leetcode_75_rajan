class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        i = n//2 - 1
        j = i+1

        c1 = c2 = 0
        vowels = set("aeiou")
     
        while i >= 0 and j < n:
            if s[i] in vowels:
                c1 += 1

            if s[j] in vowels:
                c2 += 1

            i -=1
            j+=1

        return c1==c2
        