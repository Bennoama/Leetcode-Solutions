// https://leetcode.com/problems/apply-transform-over-each-element-in-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = arr;
    const arrLen = arr.length;
    for (let i = 0; i < arrLen; i++) {
        newArr[i] = fn(arr[i], i)
    }
    return newArr;
};