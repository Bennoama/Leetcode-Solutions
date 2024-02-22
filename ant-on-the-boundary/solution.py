class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        currentPosition = 0
        count = 0
        for num in nums:
            currentPosition += num
            if currentPosition == 0:
                count += 1
        return count
