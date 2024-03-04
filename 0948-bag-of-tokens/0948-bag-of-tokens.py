class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Initialize two pointers i and j to traverse the sorted tokens list
        i = 0
        j = len(tokens) - 1
        
        # Initialize variables to keep track of the current score and the maximum score
        currScore = 0
        maxScore = 0 
        
        # Sort the tokens list in ascending order
        tokens.sort()

        # Iterate through the tokens list using two pointers
        while i <= j:
            # If the current power is sufficient to gain tokens[i], increase the score
            if power >= tokens[i]:
                power -= tokens[i]
                currScore += 1
                maxScore = max(maxScore, currScore)  # Update the maximum score
                i += 1

            # If the current score is greater than 0, try exchanging tokens with the highest value from the end
            elif currScore > 0:
                power += tokens[j]
                currScore -= 1
                j -= 1
            else:
                # If neither of the above conditions is met, break out of the loop
                break

        # Return the maximum score achieved
        return maxScore
