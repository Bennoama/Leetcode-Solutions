// https://leetcode.com/problems/apply-transform-over-each-element-in-array

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArray = [];
    let i = 0;
    for (i = 0; i < arr.length; i++) {
        newArray.push(fn(arr[i],i));
    }
    return newArray;
};