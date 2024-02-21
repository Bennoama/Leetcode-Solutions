// https://leetcode.com/problems/promise-time-limit

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        const value = fn(...args);

        const promise = new Promise ((_, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t);
        });

        return Promise.race([value, promise]);
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */