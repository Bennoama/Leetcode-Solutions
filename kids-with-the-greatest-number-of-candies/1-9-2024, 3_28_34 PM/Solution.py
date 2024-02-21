// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = [];
        maxCandies = -1;
        for item in candies:
            maxCandies = item if item > maxCandies else maxCandies
        for child in candies:
            greatest.append(child + extraCandies >= maxCandies)
        return greatest;
