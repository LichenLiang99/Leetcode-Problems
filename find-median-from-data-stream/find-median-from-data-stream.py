class MedianFinder:

    def __init__(self):
        self.x = []

    def addNum(self, num: int) -> None:
        self.x.append(num)

    def findMedian(self) -> float:
        self.x.sort()
        if len(self.x) % 2 == 1:
            return self.x[len(self.x)//2]
        else:
            i = len(self.x) // 2
            return (self.x[i] + self.x[i-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()