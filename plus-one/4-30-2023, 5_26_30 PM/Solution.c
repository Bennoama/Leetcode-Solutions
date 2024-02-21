// https://leetcode.com/problems/plus-one

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    for (int i = digitsSize - 1; i >= 0; --i)
    {
        if (9 == digits[i])
        {
            digits[i] = 0;
        }
        else
        {
            digits[i] += 1;
            break;
        }
    }
    int *new_arr;
    if (digits[0] == 0)
    {
        new_arr = (int *)malloc(sizeof(int) * (digitsSize + 1));
        memcpy((void *)(new_arr + 1), (void *)digits, digitsSize * sizeof(int));
        new_arr[0] = 1;
        *returnSize = digitsSize + 1;
    }
    else
    {
        new_arr = (int *)malloc(sizeof(int) * (digitsSize));
        memcpy((void *)(new_arr), (void *)digits, digitsSize * sizeof(int));
        *returnSize = digitsSize;
    }
    return  new_arr;
}