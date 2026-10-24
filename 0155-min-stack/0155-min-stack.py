class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = float('inf')

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minVal = min(self.minVal, value)
        self.minStack.append(self.minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.minVal = self.minStack[-1]
        else:
            self.minVal = float('inf')
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()