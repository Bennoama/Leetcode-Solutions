// https://leetcode.com/problems/summary-ranges

/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    const sumRanges = [];
    let start = 0;
    let end = 0;
    for (let i = 0; i < nums.length; i++) {
        start = nums[i];
        while (i + 1 < nums.length && nums[i] + 1 == nums[i + 1]) {
            i++;
        }
        if (start != nums[i]) {
            sumRanges.push(String(start) + "->" + String(nums[i]));
        } else {
            sumRanges.push(String(start));
        }
    }
    return sumRanges;
};