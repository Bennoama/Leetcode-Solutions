// https://leetcode.com/problems/array-prototype-last

/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    const length = this.length
    if (!length) {
        return -1;
    }
    return this[length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */