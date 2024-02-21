// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for num in arr:
            if (num in occurences):
                occurences[num] += 1
            else:
                occurences[num] = 0
        return (len(set(occurences.values())) == len(occurences.values()))