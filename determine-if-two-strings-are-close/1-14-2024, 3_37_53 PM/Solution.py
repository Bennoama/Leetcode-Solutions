// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        occur1 = [0] * 26 
        occur2 = [0] * 26
        for c in word1:
            occur1[ord(c) - ord('a')] += 1
        for c in word2:
            occur2[ord(c) - ord('a')] += 1
        for i in range(26):
            if (occur1[i] == 0 and occur2[i] != 0 or occur1[i] != 0 and occur2[i] == 0):
                return False
        occur1.sort()
        occur2.sort()

        for i in range(26):
            if occur1[i] != occur2[i]:
                return False
        return True