from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Space Complexity: O(n+k) where n is the number of players
        # Time Complexity: O(nlogn) where n is the number of matches

        # Dictionary to store the count of lost matches for each player
        lostMatches = {}

        # List to store players who have not lost any matches
        noLoss = []

        # Count the number of lost matches for each player
        for players in matches:
            winner, loser = players
            lostMatches[loser] = lostMatches.get(loser, 0) + 1

        # Identify players who have not lost any matches
        for players in matches:
            winner, loser = players
            if winner not in lostMatches:
                noLoss.append(winner)

        # Remove duplicates and sort the list of players with no loss
        noLoss = list(set(noLoss))
        noLoss.sort()

        # Filter players who lost only one match
        
        lostOneMatch = dict(filter(lambda x: x[1] == 1, lostMatches.items()))

        # Prepare the final answer as a list of lists
        answers = [[], []]
        lostOneMatch = list(lostOneMatch.keys())
        lostOneMatch.sort()
        answers[0] = list(noLoss)
        answers[1] = lostOneMatch

        return answers
