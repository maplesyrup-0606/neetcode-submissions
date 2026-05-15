class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.minel = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minel = min(self.minel, val)

    def pop(self) -> None:
        el = self.stack.pop()

        if el == self.minel:
            if self.stack:
                self.minel = min(self.stack)
            else:
                self.minel = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minel
