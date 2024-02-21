// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        std::vector<vector<int>> diffs;
        diffs.push_back(std::vector<int>());
        diffs.push_back(std::vector<int>());
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> set2(nums2.begin(), nums2.end());

        for (auto& iter : set1) {
            bool inSet2 = false;
            for (auto& iter2 : set2) {
                if (iter2 == iter) {
                    inSet2 = true;
                    break;
                }
            }
            if (!inSet2) {
                diffs[0].push_back(iter);
            }
        }

        for (auto& iter : set2) {
            bool inSet1 = false;
            for (auto& iter2 : set1) {
                if (iter2 == iter) {
                    inSet1 = true;
                    break;
                }
            }
            if (!inSet1) {
                diffs[1].push_back(iter);
            }
        }
        return diffs;
    }
};