// https://leetcode.com/problems/power-of-four

bool isPowerOfFour(int n){
    int i = 0;
    if (n == 0)
    {
        return false;
    }
    for (i = 0; i < 32; i += 2)
    {
        if (n == (n & (1 << i)))
        {
            return true;
        }
    }
    return false;
}