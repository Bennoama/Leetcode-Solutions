class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(0, len(s)):
            if self.isDivisor(s, s[:i + 1]):
                return True
        return False
        
    def isDivisor(self, s:str, divisor:str) -> bool:
        lenS = len(s)
        lenDivisor = len(divisor)
        if (lenS // lenDivisor == 1):
            return False
        res = divisor * (lenS // lenDivisor)
        return res == s
