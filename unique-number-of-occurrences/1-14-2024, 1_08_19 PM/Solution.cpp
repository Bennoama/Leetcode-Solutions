// https://leetcode.com/problems/unique-number-of-occurrences

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map <int, size_t> occurences;
        for (auto& iter : arr) {
            occurences[iter]++;
        }

        std::unordered_set<int> setOccurences;
        for (auto& iter : occurences) {
            setOccurences.insert(iter.second);
        }

        return (setOccurences.size() == occurences.size());
    }
};