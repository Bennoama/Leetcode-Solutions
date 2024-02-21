// https://leetcode.com/problems/to-be-or-not-to-be

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const toBe = (other) => { 
        if (val === other) {
            return true;
        }
        throw "Not Equal";
    }
    const notToBe = (other) => {
        if (val !== other) {
            return true;
        }
        throw "Equal";
    }
    return {'toBe': toBe, 'notToBe': notToBe};
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */