import heapq

class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []
        self.len_m = 0
        self.len_n = 0
        

    def addNum(self, num: int) -> None:
        if self.len_m == 0 or num <= -self.max[0]:
            heapq.heappush(self.max, -num)
            self.len_m+=1
        else:
            heapq.heappush(self.min, num)
            self.len_n+=1

        if (self.len_m - self.len_n) > 1:
            tmp = -heapq.heappop(self.max)
            self.len_m-=1
            heapq.heappush(self.min, tmp)
            self.len_n+=1

        if (self.len_n - self.len_m) > 1:
            tmp = heapq.heappop(self.min)
            self.len_n-=1
            heapq.heappush(self.max, -tmp)
            self.len_m+=1
        

    def findMedian(self) -> float:
        if self.len_m == self.len_n:
            return (-self.max[0] + self.min[0]) / 2
        if self.len_m > self.len_n:
            return -self.max[0]
        return self.min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()