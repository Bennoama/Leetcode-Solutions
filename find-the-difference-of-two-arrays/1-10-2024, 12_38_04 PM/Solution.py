// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = [[],[]]

        for item in set1:
            if (item not in set2):
                answer[0].append(item)
        for item in set2:
            if (item not in set1):
                answer[1].append(item)
        return answer