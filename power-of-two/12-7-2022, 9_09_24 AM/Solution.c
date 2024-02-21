// https://leetcode.com/problems/power-of-two

bool isPowerOfTwo(int n){
    if (n == -2147483648)
    {
        return 0;
    }
    return ((0 != n) && !(n & (n-1)));
}