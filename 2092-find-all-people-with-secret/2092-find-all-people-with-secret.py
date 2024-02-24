class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        # Path compression
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def reset(self, node):
        # Resetting the parent to the node itself
        self.parent[node] = node

    def union(self, nodea, nodeb):
        apar, bpar = self.find(nodea), self.find(nodeb)
        # Union by rank
        if apar != bpar:
            if self.rank[apar] < self.rank[bpar]:
                self.parent[apar] = bpar
            elif self.rank[apar] > self.rank[bpar]:
                self.parent[bpar] = apar
            else:
                self.parent[apar] = bpar
                self.rank[bpar] += 1


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sorting meetings based on time in ascending order
        meetings.sort(key=lambda x: x[2])

        dsu = DSU(n)
        dsu.union(0, firstPerson)

        i = 0
        while i < len(meetings):
            ct = meetings[i][2]
            curPeople = []

            # Processing meetings at the same time
            while i < len(meetings) and meetings[i][2] == ct:
                dsu.union(meetings[i][0], meetings[i][1])
                curPeople.extend([meetings[i][0], meetings[i][1]])
                i += 1

            # Resetting people who don't share the secret
            for curPep in curPeople:
                if dsu.find(curPep) != dsu.find(0):
                    dsu.reset(curPep)

        # Finding all people who know the secret after meetings
        ans = [i for i in range(n) if dsu.find(i) == dsu.find(0)]
        return ans
