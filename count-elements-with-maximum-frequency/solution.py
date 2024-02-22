class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        newMap = {}
        for num in nums:
            if num in newMap:
                newMap[num] += 1
            else:
                newMap[num] = 1
        maxFreq = 0
        count = 0
        for key, value in newMap.items():
            if maxFreq < value:
                count = 1
                maxFreq = value
            elif maxFreq == value:
                count += 1

        return maxFreq * count
