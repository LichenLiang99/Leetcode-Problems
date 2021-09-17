class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:    
        q2 = self.q
        q2.append(x)
        for _ in range(len(q2) - 1):
            self.q.append(q2.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not len(self.q)

        #time: o(n) for push, o(1) for others, space o(1)
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()