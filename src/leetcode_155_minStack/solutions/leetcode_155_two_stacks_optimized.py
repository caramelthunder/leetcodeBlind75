class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or self.minimum[-1][0] > val:
            self.minimum.append([val, 1])

        elif self.minimum[-1][0] == val:
            self.minimum[-1][1] += 1

    def pop(self) -> None:
        if self.minimum[-1][0] == self.stack[-1]:
            self.minimum[-1][1] -= 1
        
        if self.minimum[-1][1] == 0:
            self.minimum.pop()

        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1][0]
