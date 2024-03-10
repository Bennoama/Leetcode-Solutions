class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        count1 = 1
        arr2 = [nums[1]]
        count2 = 1
        for i in range(2, len(nums)):
            if arr1[count1 - 1] > arr2[count2 - 1]:
                arr1.append(nums[i])
                count1 += 1
            else:
                arr2.append(nums[i])
                count2 += 1
        return arr1 + arr2
