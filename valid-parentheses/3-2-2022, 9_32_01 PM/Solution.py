// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        booly = True
        for c in s:
            if c == '(' or c =='[' or c =='{':
                stack.append(c)
            elif (c == ')' or c ==']' or c =='}') and len(stack) ==0:
                return False
            elif c == ')':
                if stack.pop() != '(':
                    booly = False
            elif c == ']':
                if stack.pop() != '[':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    booly = False
        return booly and len(stack)==0