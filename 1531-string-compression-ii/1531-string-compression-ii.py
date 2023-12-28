class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Time complexity: O(n*k*N)
        # Space complexity: O(n*k*N)
        cache = {}

        def countMinLength(i, k, prevChar, prevCharCount):
            if (i, k, prevChar, prevCharCount) in cache:
                return cache[(i, k, prevChar, prevCharCount)]

            # Base Case : if limit of K is over, we have no more deletiosn left
            if k < 0:
                return float("inf")

            # Base Case : out of bounds
            if i == len(s):
                return 0

            # if both curr and prev char matches
            if s[i] == prevChar:
                incr = 1 if prevCharCount in [1, 9, 99, 999] else 0
                res = incr + countMinLength(i+1, k, prevChar, prevCharCount+1)

            elif s[i] != prevChar:
                # Two possible options to execute
                # 1.) To include the curr char s[i] and proceed
                # 2.) To delete the curr char s[i] and proceed 

                res = min(
                        (1 + countMinLength(i+1, k, s[i], 1)),
                        countMinLength(i+1, k-1, prevChar, prevCharCount)
                        )
            cache[(i, k, prevChar, prevCharCount)] = res
            return res
        return countMinLength(0, k, "", 0)



###### NEETCODE CODE BELOW ########

# class Solution:      
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#         cache= {}
#         # 0(n*k*)
#         def count(i, k, prev, prev_cnt):
#             if (i, k, prev, prev_cnt) in cache:
#                 return cache [ (i, k, prev, prev_cnt)]
#             if k < 0:
#                 return float("inf")
#             if i == len(s):
#                 return 0
#             if s[i] == prev:
#                 incr = 1 if prev_cnt in [1, 9, 99] else 0
#                 res = incr + count(i + 1, k, prev, prev_cnt + 1)
#             else:
#                 res = min (
#                     count(i + 1, k- 1, prev, prev_cnt), # delete s[i]
#                     1 + count(i + 1, k, s[i], 1)) # dont delete
#             cache[(i, k, prev, prev_cnt)] = res
#             return res
#         return count(0, k,"" ,0)



###### Just code for string Compression alone : ######

# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#         rle = ""
#         counter = 1
#         for i in range(0,len(s)-1):            
#             if s[i] == s[i+1]:
#                 counter+=1
#                 if i == len(s)-2:
#                     rle += s[i] + str(counter)
#             else:
#                 rle += s[i] + str(counter) if counter>1 else s[i] 
#                 if i == len(s)-2:
#                     rle += s[i+1] 
#                 counter = 1
#         print(rle)
#         return rle
#         # returns a3bc3d for aaabcccd


'''

Approach
Example Input:
* s = "aaabcccd"
* k = 2

1.) Initialization:

Initialize the cache to store intermediate results.
Start the recursive function by calling countMinLength(0, k, "", 0).
2.) Recursive Function:

Base Cases:

If k is less than 0, return float("inf") since we cannot perform more deletions.
If we have reached the end of the string (i == len(s)), return 0, as there is nothing more to compress.
3.) Matching Characters:

Check if the current character s[i] matches the previous character prevChar.

If they match, calculate the increment (incr) based on the count of consecutive characters, and recursively call the function with the incremented count.

4.) Non-Matching Characters:

If the current character doesn't match the previous one, consider two options:

Include the current character s[i] and proceed with a count of 1.
Delete the current character s[i] and proceed with the previous character and an incremented count.
5.) Cache:

Store the result in the cache for memoization to avoid redundant calculations.
Return Result : Return the minimum result among the two options.
6.) Example Execution:

For the input "aaabcccd" and k = 2, the function starts with an empty previous character ("") and count (0).

It first encounters "a" and "a," and since they match, it calculates the increment and proceeds with the next character.

The recursion continues until it encounters "b," where it considers both including and deleting "b."

The recursion explores various possibilities, memoizing results in the cache.
Final Result:

Quote
The function returns the minimum length of the compressed string.
This code essentially explores different possibilities of compressing the string while considering the constraints on deletions and consecutive character counts. The memoization using the cache helps avoid redundant computations and improves the efficiency of the algorithm.

Complexity
Time complexity: O(nkN)
Space complexity: O(nkN)


'''

        