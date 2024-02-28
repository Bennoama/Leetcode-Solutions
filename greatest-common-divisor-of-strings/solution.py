class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortS = ""
        longS = ""

        if len(str1) > len(str2):
            shortS = str2
            longS = str1
        else:
            shortS = str1
            longS = str2

        for i in range(len(shortS) - 1, -1, -1):
            if (self.isDivisor(str1, shortS[:i + 1]) and self.isDivisor(str2, shortS[:i + 1])):
                return shortS[:i + 1]
        return ""

    def isDivisor(self, s:str, divisor:str) -> bool:
        lengthS = len(s)
        lengthDivisor = len(divisor)
        if (lengthDivisor == 0):
            return False
        numTimes = lengthS // lengthDivisor

        acc = ""
        for i in range(0, numTimes):
            acc += divisor
        
        return acc == s
