class MedianFinder:

    def __init__(self):
        self.mid = -1
        self.is_even = True
        self.stream = []

    def addNum(self, num: int) -> None:
        if not self.stream:
            self.stream.append(num)
        else:
            i=0
            while i < len(self.stream) and self.stream[i] < num:
                i+=1
            self.stream.insert(i, num)
        if self.is_even:
            self.mid += 1
        self.is_even = not self.is_even

    def findMedian(self) -> float:
        if self.is_even:
            return (self.stream[self.mid] + self.stream[self.mid + 1]) / 2
        return self.stream[self.mid]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()