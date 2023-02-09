class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []
        self.first = None

    def push(self, val):
        if not self.stackA:
            self.first = val
        self.stackA.append(val)
    
    def pop(self) -> int:
        if self.empty():
            return None

        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        return self.stackB.pop()
    
    def peek(self) -> int:
        if self.stackB:
            return self.stackB[-1]
        return self.first
    
    def empty(self) -> bool:
        return not (self.stackA or self.stackB)