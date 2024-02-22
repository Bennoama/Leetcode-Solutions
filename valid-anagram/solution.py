class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in dictS:
                dictS[c] = 1
            else:
                dictS[c] += 1
        
        for c in t:
            if c not in dictT:
                dictT[c] = 1
            else:
                dictT[c] += 1

        for key, value in dictS.items():
            if key not in dictT:
                return False
            if value != dictT[key]:
                return False

        return True
