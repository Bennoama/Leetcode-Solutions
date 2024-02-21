// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        subStrings = s.split(" ");
        myDict = dict();

        if (len(subStrings)) != len(pattern):
            return False;
        
        if (len(set(pattern)) != len(set(subStrings))):
            return False;

        i = 0;
        while (i < len(pattern) and i < len(s)):
            if (pattern[i] not in myDict):
                myDict[pattern[i]] = subStrings[i];
            elif (myDict[pattern[i]] != subStrings[i]):
                return False;
            i += 1;
        return True;