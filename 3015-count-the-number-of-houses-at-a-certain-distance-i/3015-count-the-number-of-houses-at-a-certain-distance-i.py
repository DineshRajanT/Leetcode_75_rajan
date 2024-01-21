from typing import List

class Solution:
    # T : O(n^3)
    # S : O(n^2)
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # Initialize the matrix with all distances set to infinity.
        mat = [[float("inf")] * (n+1) for _ in range(n+1)]

        # Initialize the matrix for direct connections between houses.
        for i in range(2, n+1):
            j = i - 1
            mat[i][i] = 0
            mat[j][j] = 0
            mat[i][j] = 1
            mat[j][i] = 1

        # Add the direct connection between house x and house y.
        if x != y:
            mat[x][y] = 1
            mat[y][x] = 1

        # Initialize a dictionary to count the occurrences of each distance.
        distCounts = {k: 0 for k in range(n+1)} # including zero distance also because node to node self-distance is zero
        print(distCounts)

        # Apply the Floyd-Warshall algorithm to find the shortest paths.
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

        ## Print the resulting distance matrix.
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         print(mat[i][j], end=" ")
        #     print()

        # Count the occurrences of each distance in the matrix.
        for i in range(1, n+1):
            for j in range(1, n+1):
                distCounts[mat[i][j]] = distCounts.get(mat[i][j], 0) + 1
        print(distCounts)

        # Create a list of counts for distances 1 to n (excluding zero distance).
        ans = []
        for i in range(1, n+1):
            ans.append(distCounts[i])

        print(ans)

        return ans


