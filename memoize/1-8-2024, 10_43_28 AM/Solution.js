// https://leetcode.com/problems/memoize

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const map = new Map();
    return function(...args) {
        const argsAsString = JSON.stringify(args);
        if (argsAsString in map) {
            return map[argsAsString];
        }
        const ret = fn(...args);
        map[argsAsString] = ret;
        return ret;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */