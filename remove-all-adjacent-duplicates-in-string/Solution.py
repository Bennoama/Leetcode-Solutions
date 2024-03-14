class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = ""
        for c in s:
            if len(stack) >= 1 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        for char in stack:
            res += char
        return res
            
