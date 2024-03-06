class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for oper in operations:
            match oper:
                case '+':
                    stack.append(stack[-1] + stack[-2])
                case 'D':
                    stack.append(2 * stack[-1])
                case 'C':
                    stack.pop()
                case _: #default
                    stack.append(int(oper))
        
        return sum(stack)
