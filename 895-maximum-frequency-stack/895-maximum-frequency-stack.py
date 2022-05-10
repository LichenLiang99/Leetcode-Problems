class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxF = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxF = max(self.maxF, self.freq[val])
        self.m[self.freq[val]].append(val)
        
    def pop(self) -> int:
        x = self.m[self.maxF].pop()
        if not self.m[self.maxF]: 
            self.maxF = self.maxF - 1
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()