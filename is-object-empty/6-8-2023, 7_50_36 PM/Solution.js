// https://leetcode.com/problems/is-object-empty

/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    return (0 === obj.length && !obj.hasOwnProperty('length') || _.isEmpty(obj));
};