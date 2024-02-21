// https://leetcode.com/problems/number-of-1-bits

class Solution {
public:
    int hammingWeight(uint32_t n) {
        if (!n){
            return 0;
        }
        int count = 0;
        while (n) {
            ++count;
            n &= n - 1;
        }
        return count;
    }
};