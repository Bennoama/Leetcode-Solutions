// https://leetcode.com/problems/unique-number-of-occurrences

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map <int, size_t> occurences;
        for (auto& iter : arr) {
            occurences[iter]++;
        }

        std::unordered_set<int> setOccurences;
        size_t numOccurences = 0;
        for (auto& iter : occurences) {
            setOccurences.insert(iter.second);
            numOccurences++;
        }

        return (setOccurences.size() == numOccurences);
    }
};