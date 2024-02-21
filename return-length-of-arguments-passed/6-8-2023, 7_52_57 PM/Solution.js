// https://leetcode.com/problems/return-length-of-arguments-passed

/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    let i = 0;
    for (const _ in args) {
        i++;
    }
    return i;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */