// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_length = min([len(l) for l in strs])
        for index in range(min_length):
            all_letters = [word[index] for word in strs]
            letters = set(all_letters)
            if len(letters) == 1:
                prefix += all_letters[0]
            else:
                return prefix
        return prefix