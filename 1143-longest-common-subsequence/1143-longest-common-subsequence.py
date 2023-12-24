class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1) # rows
        M = len(text2) # cols
        LCS = [[""]*(M+1) for i in range(N+1)]
        # +1 # Adding 1 to accomodate "" (space character) 
        # if the character matches then take the diagonal value and append the curr value with it
        # else if the characters doesn't match take the maximum len of i-1, j-1 (i.e) left cell and upper cell
        for i in range(N+1):
            for j in range(M+1):
                if i==0 or j==0: # for the extra empty row and empty column
                    LCS[i][j] = ""
                elif text1[i-1] == text2[j-1]: 
                    LCS[i][j] = LCS[i-1][j-1] + text1[i-1] # take diagonal + curr
                else:
                    LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1], key=len) 

        return len(LCS[N][M])



        
    ### Count of lens alone here...

    #     m = len(text1)
    #     n = len(text2)
    #     L = [[None]*(n+1) for i in range(m+1)]
 
    # # Following steps build L[m+1][n+1] in bottom up fashion
    # # Note: L[i][j] contains length of LCS of X[0..i-1]
    # # and Y[0..j-1]
    #     for i in range(m+1):
    #         for j in range(n+1):
    #             if i == 0 or j == 0:
    #                 L[i][j] = 0
    #             elif text1[i-1] == text2[j-1]:
    #                 L[i][j] = L[i-1][j-1]+1
    #             else:
    #                 L[i][j] = max(L[i-1][j], L[i][j-1])
    
    #     # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    #     return L[m][n]

    



        