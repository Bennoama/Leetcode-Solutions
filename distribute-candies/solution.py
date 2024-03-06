class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        length = len(candyType)
        candySet = set(candyType)

        amountCanEat = length // 2

        return amountCanEat if len(candySet) >= amountCanEat else len(candySet)
