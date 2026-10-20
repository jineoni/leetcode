class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.pop(0))

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()