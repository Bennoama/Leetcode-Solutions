class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        for num in nums:
            if maxNum < 2 * num and maxNum != num:
                return -1
        return nums.index(maxNum)
