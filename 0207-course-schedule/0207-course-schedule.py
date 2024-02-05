from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a dictionary to store prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Populate the dictionary with prerequisites
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # Set to keep track of visited nodes during DFS
        visitSet = set()

        # Define a depth-first search (DFS) function
        def dfs(course):
            # If the course is already visited, there is a cycle
            if course in visitSet:
                return False
            # If there are no prerequisites for the course, it's reachable
            if preMap[course] == []:
                return True

            # Mark the course as visited
            visitSet.add(course)

            # Recursively check prerequisites
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            # Remove the course from the visited set and mark it as completed
            visitSet.remove(course)
            preMap[course] = []
            return True

        # Iterate through each course and check if it can be completed
        for each_course in range(numCourses):
            if not dfs(each_course):
                return False

        # If all courses can be completed without a cycle, return True
        return True

# Time complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges)
# Space complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges)
