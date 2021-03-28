class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.min.append(self.stack[0])
        else:
            self.min.append(min(self.min[-1], self.stack[-1]))    

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())