class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.minel = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minel = val
        else:
            self.stack.append(val - self.minel)
            if val < self.minel:
                self.minel = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.minel = self.minel - pop

    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.minel
        
        else: 
            return self.minel

    def getMin(self) -> int:
        return self.minel
