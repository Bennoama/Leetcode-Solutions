// https://leetcode.com/problems/array-prototype-last

Array.prototype.last = function() {
    const arrLength = this.length;
    if (!arrLength) {
        return -1;
    }
    return this[arrLength - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */