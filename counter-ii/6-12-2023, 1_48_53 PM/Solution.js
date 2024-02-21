// https://leetcode.com/problems/counter-ii

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
/*
function increment(this_) {
    this_.value++;
    return this_.value;
}
*/
var createCounter = function(init) {
    const object = new Object;
    object.init = init;
    object.value = init;
    object.increment = function(){
        return ++this.value;
    }
    object.decrement = function(){
        return --this.value;
    }
    object.reset = function(){
        return (this.value = this.init);
    }
    return object;
    };

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */