class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letterMap = {}
        for c in s:
            if c in letterMap:
                letterMap[c] += 1
            else:
                letterMap[c] = 1
        for c in t:
            if c not in letterMap:
                return c
            elif letterMap[c] == 0:
                return c
            else:
                letterMap[c] -= 1
