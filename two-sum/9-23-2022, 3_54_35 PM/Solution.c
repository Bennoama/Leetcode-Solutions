// https://leetcode.com/problems/two-sum



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    returnSize = (int *)calloc(2, sizeof(int));
    int i = 0;
    int j = 0;
    for (i = 0; i < numsSize-1; i++)
    {
        for (j = i+1; j < numsSize; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                returnSize[0] = i;
                returnSize[1] = j;
                break;
            }
        }
    }
    return returnSize;
}