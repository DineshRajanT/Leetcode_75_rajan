from queue import Queue
from typing import List

# Time complexity is O((k+1) * V), which can be simplified to O(k * V)
# Space complexity is O(V)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create an adjacency list to represent the graph
        gr = [[] for _ in range(n)]
        for e in flights:
            gr[e[0]].append((e[1], e[2]))

        # Initialize distance array with infinity
        dist = [float('inf')] * n
        # Create a queue for BFS
        q = Queue()
        # Start from source node with distance 0
        q.put((src, 0))  # (node, distance)
        stops = 0

        # Perform BFS with a maximum of k stops
        while stops <= k and not q.empty():
            sz = q.qsize()
            while sz > 0:
                node, distance = q.get()
                sz -= 1
                # Explore neighbors of the current node
                for neighbour, price in gr[node]:
                    # Update the distance if a shorter path is found
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.put((neighbour, dist[neighbour]))
            stops += 1

        # Return the final distance to the destination node or -1 if not reachable
        return dist[dst] if dist[dst] != float('inf') else -1





# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         adj_list = defaultdict(list)
#         costs = defaultdict(list)
#         cache = defaultdict(int)

#         for flight in flights:
#             adj_list[flight[0]].append(flight[1])
#             costs[flight[0]].append(flight[2])
        
#         def dfs(node, hops, curr_cost):
#             if cache[node, hops, curr_cost] !=0:
#                 return cache[node, hops, curr_cost]

#             if hops > k+1: 
#                 return float('inf')

#             if node == dst:
#                 return curr_cost

#             min_cost = float('inf')

#             for neighbor, cost in zip(adj_list[node], costs[node]):
#                 result = dfs(neighbor, hops + 1, curr_cost + cost)
#                 min_cost = min(min_cost, result)

#             cache[node, hops, curr_cost] = min_cost

#             return min_cost

#         result = dfs(src, 0, 0)
        
#         return -1 if result == float('inf') else result
