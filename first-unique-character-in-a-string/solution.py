class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict = {}
        length = len(s)
        for i in range(0, length):
            if s[i] in myDict:
                myDict[s[i]] = length
            else:
                myDict[s[i]] = i
        minIndex = length
        for key, value in myDict.items():
            minIndex = min(minIndex, value)
        return minIndex if minIndex != length else -1
