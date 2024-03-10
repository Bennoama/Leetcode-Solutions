class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxVal = 0
        for s in strs:
            currVal = self.getStringValue(s)
            maxVal = currVal if currVal > maxVal else maxVal
        return maxVal

    def getStringValue(self, s:str) -> int:
        if s.isdigit():
            return int(s)
        return len(s)
