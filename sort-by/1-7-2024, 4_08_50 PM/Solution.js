// https://leetcode.com/problems/sort-by

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((n1, n2) => { return fn(n1) - fn(n2)})
};