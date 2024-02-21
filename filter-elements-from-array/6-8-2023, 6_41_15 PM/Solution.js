// https://leetcode.com/problems/filter-elements-from-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    for (let i = arr.length; i >= 0; i--) {
        if (!fn(arr[i], i)) {
            arr.splice(i, 1);
        }
    }
    return arr;
};