class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        removed = ""
        stack = []
        for c in s:
            if c == '(':
                if len(stack) != 0:
                    removed += c
                stack.append(c)
            else: # ')'
                stack.pop()
                if len(stack) != 0:
                    removed += c
        return removed
