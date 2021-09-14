class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.maxSize:
            self.s.append(x)

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1
        return self.s.pop()
        

    def increment(self, k: int, val: int) -> None:
        size = min(k, len(self.s))
        for i in range(size):
            self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)