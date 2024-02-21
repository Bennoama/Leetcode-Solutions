// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}
        for i in range(0, len(s)):
            if (s[i] in charMap):
                if t[i] != charMap[s[i]]:
                    return False
            elif t[i] in list(charMap.values()):
                return False
            else:
                charMap[s[i]] = t[i]

        return True
