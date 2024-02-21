// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = "";
        i = 0;
        j = 0;
        len1 = len(word1);
        len2 = len(word2);
        firstWord = True;
        while (i < len1 and j < len2):
            if (firstWord):
                merged += word1[i];
                i += 1;
            else:
                merged += word2[j];
                j += 1;
            firstWord = not firstWord;
        while (i < len1):
            merged += word1[i];
            i += 1;
        while (j < len2):
            merged += word2[j];
            j += 1;
        return merged;