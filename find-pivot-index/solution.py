class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        rightSum = totalSum - nums[0]
        if rightSum == 0:
            return 0
        leftSum = 0
        for i in range(1, len(nums)):
            leftSum += nums[i - 1]
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
        return -1
            
