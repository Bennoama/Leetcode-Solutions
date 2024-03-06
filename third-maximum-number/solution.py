class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        newSet = set(nums)
        if len(newSet) < 3:
            return max(newSet)
        newSet.remove(max(newSet))
        newSet.remove(max(newSet))
        return max(newSet)
