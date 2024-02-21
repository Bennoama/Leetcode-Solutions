// https://leetcode.com/problems/counting-bits

class Solution {
public:

    size_t CountNumBitsOn(int i){
        size_t count = 0;
        if (!i){
            return 0;
        }
        while (i) {
            ++count;
            i &= (i - 1);
        }
        return count;
    }
    vector<int> countBits(int n) {
        vector<int> ans;
        for (size_t i = 0; i <= n; ++i){
            ans.push_back(CountNumBitsOn(i));
        }
        return ans;
    }
};