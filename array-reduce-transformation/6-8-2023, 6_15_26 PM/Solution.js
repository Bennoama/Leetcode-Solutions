// https://leetcode.com/problems/array-reduce-transformation

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    const numsLen = nums.length;
    if (!numsLen) {
        return init;
    }
    let val = fn(init, nums[0]);
    for (let i = 1; i != numsLen; i++) {
        val = fn(val, nums[i]);
    }
    return val;
};