// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.Stack = []
        
    def push(self, val: int) -> None:
        self.Stack += [val]
        
    def pop(self) -> None:
        self.Stack = self.Stack[:-1]

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        minimum_number = 2**31-1
        for item in self.Stack:
            if item < minimum_number:
                minimum_number = item
        return minimum_number
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()