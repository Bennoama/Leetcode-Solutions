class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if self.hasTrailZero(num):
                if (count == 1):
                    return True
                count = 1
        return False

    def hasTrailZero(self, num: int):
        return num & 1 == 0
