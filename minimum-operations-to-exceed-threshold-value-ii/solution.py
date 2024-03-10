import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while (len(nums) >= 2):
            if nums[0] >= k:
                return count
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
            curr = min(min1, min2) * 2 + max(min1, min2)
            heapq.heappush(nums, curr)
            count += 1
        return count
