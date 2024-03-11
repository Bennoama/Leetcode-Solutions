class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[::]
        expected.sort()
        counter = 0
        for i in range(0, len(heights)):
            if expected[i] != heights[i]:
                counter += 1
        return counter
