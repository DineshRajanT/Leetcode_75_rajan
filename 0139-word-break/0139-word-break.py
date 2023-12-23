from typing import List

class Solution:
    #Time Complexity: O(n * m)
    # Space Complexity: O(n)
    '''
    Initialization:

    n = len(s): Get the length of the input string s.
    dp = [False] * (n + 1): Initialize a boolean array dp of size n + 1. This array will be used to store whether the substring ending at position i can be segmented into words from the dictionary.

    Base Case:
    dp[0] = True: An empty string can always be segmented, so we set dp[0] to True.

    Dynamic Programming Loop:
    for i in range(1, n + 1):: 
        Iterate over each position in the string.
    for word in wordDict:: 
        Iterate over each word in the dictionary.
    if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word::
        Check if the current position i is greater than or equal to the length of the current word (len(word)).
        Check if the substring ending at position i - len(word) can be segmented (dp[i - len(word)] is True).
        Check if the substring from i - len(word) to i matches the current word.
        dp[i] = True: If all conditions are met, set dp[i] to True.
        break: Once a match is found, no need to check other words for the current position i.
        
    Result:
    return dp[n]: The final result is stored in dp[n], indicating whether the entire string can be segmented into words from the dictionary.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # base case (i.e) an empty string can always be segemnted....

        for i in range(1, n+1):
            for word in wordDict:
                if i>=len(word) and dp[i - len(word)] and s[i -len(word) : i] == word:
                    dp[i] = True
                    break
        return dp[n]
        

# class Solution:
        
#     def LongPrefixSuffix(self, subString):
#         LPS = [0] * len(subString)
#         prevLPS, i = 0, 1
#         while i < len(subString):
#             if subString[i] == subString[prevLPS]:
#                 LPS[i] = prevLPS + 1
#                 prevLPS += 1
#                 i+=1
#             else:
#                 if prevLPS == 0:
#                     LPS[i] = 0
#                     i+=1
#                 else:
#                     prevLPS = LPS[prevLPS-1]
#         return LPS

#     def checkSubString(self, s, word):
#         lps = self.LongPrefixSuffix(word)
#         i = 0
#         j = 0

#         while i < len(s):
#             if s[i] == word[j]:
#                 i+=1
#                 j+=1
#             else:
#                 if j==0:
#                     i+=1
#                 else:
#                     j = lps[j-1]
#             if j == len(word):
#                 return i- len(word)
#         return -1


#     def isPartOfString(self, s, word):
#         indexOfSubString = self.checkSubString(s, word)
#         return indexOfSubString


#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         Indices = []
#         counter_S =0
#         s_copy = s
#         while s:
#             for i in range(len(wordDict)):
#                 word = wordDict[i]
#                 Idx = self.isPartOfString(s, word)
#                 Indices.append(Idx)
#                 print(Indices)
#                 if Idx >=0:
#                     counter_S += len(word)
#                     s = s[0:Idx] + s[Idx+len(word):]
#                     print("String :",s)
#                     print(counter_S)
                    
#             if Indices[-1]==-1:
#                 break

#         if counter_S == len(s_copy):
#             return True
#         return False 
        