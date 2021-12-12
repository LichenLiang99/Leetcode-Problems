class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        self.pt = []
    def add(self, point: List[int]) -> None:
        
        self.points[tuple(point)] += 1
        self.pt.append(point)
        
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pt:
            if (abs(py - y) != abs(px - x)) or px == x or py == y:
                continue
            res += self.points[(x, py)] * self.points[(px, y)]
        return res
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)