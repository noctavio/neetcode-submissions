class MedianFinder:

    def __init__(self):
        self.lHalfHeap = [] # maxHeap (multiply elements by -1)
        self.rHalfHeap = [] # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lHalfHeap, -1 * num)

        heapsNotNull = (self.lHalfHeap and self.rHalfHeap)
                        # compares if last val of left half 
                        # with first val of right half

        if (heapsNotNull and (-1 * self.lHalfHeap[0]) > self.rHalfHeap[0]):
            val = -1 * heapq.heappop(self.lHalfHeap) # cast -1 to normalize val
            heapq.heappush(self.rHalfHeap, val)

        if len(self.lHalfHeap) > len(self.rHalfHeap) + 1:
            val = -1 * heapq.heappop(self.lHalfHeap) # cast -1 to normalize val
            heapq.heappush(self.rHalfHeap, val)
        if len(self.rHalfHeap) > len(self.lHalfHeap) + 1:
            val = heapq.heappop(self.rHalfHeap)
            heapq.heappush(self.lHalfHeap, -1 * val) # cast by -1 before adding!

    def findMedian(self) -> float:
        if len(self.lHalfHeap) > len(self.rHalfHeap):
            return -1 *self.lHalfHeap[0]
        if len(self.rHalfHeap) > len(self.lHalfHeap):
            return self.rHalfHeap[0]
        
        return (-1 * self.lHalfHeap[0] + self.rHalfHeap[0]) / 2


        