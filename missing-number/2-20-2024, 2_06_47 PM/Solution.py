// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        n = len(nums)
        a1 = 0
        arithmeticSequenceSum = (((n + 1) - a1) / 2) * n

        return int(arithmeticSequenceSum - sum(nums))