// https://leetcode.com/problems/power-of-three

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 1){
            return true;
        }
        if (n <= 0)
        {
            return false;
        }
        while (n){
            if (n % 3 != 0 && n != 1){
                return false;
            } else {
                n /= 3;
            }
        }
        return true;
    }
};