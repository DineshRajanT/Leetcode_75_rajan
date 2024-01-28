class Solution:
    def isPalindrome(self, s: str) -> bool:

        def formatStr(x):
            x_ = ""
            for char in x:
                if char.isalnum():
                    x_ += char.lower()
            return x_



        newStr = formatStr(s)
        print(newStr)

        i = 0
        j = len(newStr) - 1

        while i < j:
            if newStr[i] != newStr[j]:
                return False
            i+=1
            j-=1
        return True

        