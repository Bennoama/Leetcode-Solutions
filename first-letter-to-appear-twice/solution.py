class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letterMap = {}
        for c in s:
            if c in letterMap:
                return c
            letterMap[c] = 1
        return ''
