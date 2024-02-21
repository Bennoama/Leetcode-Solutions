// https://leetcode.com/problems/majority-element

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> map;
        for (auto& iter : nums) {
            if (++map[iter] > nums.size() / 2){
                return iter;
            }
        }
    return 0;
    }
};