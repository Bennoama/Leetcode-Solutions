// https://leetcode.com/problems/climbing-stairs


int climbStairs(int n){
    size_t a = 1; size_t b = 1;
    for (size_t i = 0; i < n; ++i) {
        size_t temp = a;
        a += b;
        b = temp;
    }
    return b;
}