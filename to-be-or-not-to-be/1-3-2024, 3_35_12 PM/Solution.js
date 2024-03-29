// https://leetcode.com/problems/to-be-or-not-to-be

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (value) => {
            if (value === val) {
                return true;
            }
            throw "Not Equal";
        },
        notToBe: (value) => {
            if (value !== val) {
                return true;
            }
            throw "Equal";
        }};
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */