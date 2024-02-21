// https://leetcode.com/problems/single-number

int singleNumber(int* nums, int numsSize){
    int xor_val = 0;
    for (int i = 0; i <numsSize; ++i)
    {
        xor_val ^= nums[i];
    }
    return xor_val;
}