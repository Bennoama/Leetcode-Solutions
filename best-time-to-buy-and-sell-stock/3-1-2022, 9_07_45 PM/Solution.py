// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0
        for right in range(len(prices)):
            if prices[right]-prices[left] > profit:
                profit = prices[right]-prices[left]
            if prices[right] < prices[left]:
                left = right
        return profit