from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights)
        min_heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                # If ladders are available, use them
                if ladders > 0:
                    heapq.heappush(min_heap, diff)
                    ladders -= 1

                # If no ladders, use bricks when needed
                elif min_heap and diff > min_heap[0]:
                    heapq.heappush(min_heap, diff)
                    bricks -= heapq.heappop(min_heap)

                # If no ladders and bricks, stop
                else:
                    bricks -= diff

                # If not enough bricks, return the current index
                if bricks < 0:
                    return i

        # If all buildings can be reached, return the last index
        return n - 1

# Time complexity: O(N log K), where N is the number of buildings and K is the number of ladders
# Space complexity: O(K), where K is the number of ladders (for the min heap)
