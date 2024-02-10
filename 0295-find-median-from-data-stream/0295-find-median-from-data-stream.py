import heapq

class MedianFinder:

    def __init__(self):
        # Initialize two heaps: small to store the smaller half of the elements and large to store the larger half.
        self.small, self.large = [], []
        # small is MaxHeap
        # large is MinHeap

    def addNum(self, num: int) -> None:
        # Push the negation of the number to the small heap.
        heapq.heappush(self.small, -1 * num)

        # Balance the heaps by moving the maximum element from small to large if necessary.
        if (self.small and self.large and
           (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Ensure that the size difference between the heaps is at most 1.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If the size of the small heap is greater, return the maximum element (negated) from the small heap.
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # If the size of the large heap is greater, return the minimum element from the large heap.
        if len(self.large) > len(self.small):
            return self.large[0]

        # If the sizes are equal, return the average of the maximum from small and minimum from large.
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# Space Complexity:
# The space complexity is O(n), where n is the number of elements added. 
# In the worst case, all elements might end up in one heap.

# Time Complexity:
# - addNum: O(log n) for each call, where n is the total number of elements.
#   The heappush and heappop operations have logarithmic time complexity.
# - findMedian: O(1), as we are directly accessing the maximum and minimum elements from the heaps.
