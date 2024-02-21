// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        check = False
        while i < len(nums):
            if nums[i] == nums[i-1]:
                if check == True:
                    nums.remove(nums[i])
                else:
                    check = True
                    i += 1
            else:
                check = False
                i+=1
        return len(nums)
            