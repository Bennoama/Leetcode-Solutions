// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorSum = 0
        for x in nums:
            xorSum ^= x
        return xorSum