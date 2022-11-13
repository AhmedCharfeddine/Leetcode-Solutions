class MedianFinder:

    def __init__(self):
        self.small_heap = []    # contains the negative of the actual nums
        self.big_heap = [] 
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)
                
        # removal condition: num should be in big heap or lengths are close
        if len(self.small_heap) > len(self.big_heap) + 1 or (self.big_heap and -self.small_heap[0] > self.big_heap[0]):
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        
        # removal condition: if max heap's length execeeds min heap length by 2
        if len(self.small_heap)+1 < len(self.big_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))
        
    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.big_heap):
            return -self.small_heap[0]
        elif len(self.small_heap) < len(self.big_heap):
            return self.big_heap[0]
        return (-self.small_heap[0]+self.big_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()