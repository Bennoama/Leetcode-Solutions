// https://leetcode.com/problems/ransom-note

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> map;
        for(size_t i = 0; i < magazine.length(); ++i){
            ++map[magazine[i]];
        }
        for (size_t i = 0; i < ransomNote.length(); ++i){
            if (-1 == (--map[ransomNote[i]])){
                return false;
            }
            
        }
        return true;
    }
};