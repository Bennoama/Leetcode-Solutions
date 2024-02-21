// https://leetcode.com/problems/merge-sorted-array

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        size_t runner1 = 0;
        size_t runner2 = 0;
        std::vector<int> temp;
        while (runner1 < m && runner2 < n){
            if (nums1[runner1] <= nums2[runner2]){
                temp.push_back(nums1[runner1++]);
            } else {
                temp.push_back(nums2[runner2++]);
            }
        }
        while (runner1 < m)
        {
            temp.push_back(nums1[runner1++]);
        }
        while (runner2 < n)
        {
            temp.push_back(nums2[runner2++]);
        }
        for (size_t i = 0; i < m + n; ++i)
        {
            nums1[i] = temp[i];
        }
    }
};