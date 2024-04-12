// 2630. Memoize II
// 
// Given a function fn, return a memoized version of that function.
// 
// A memoized function is a function that will never be called twice with the 
// same inputs. Instead it will return a cached value.
// 
// fn can be any function and there are no constraints on what type of values it 
// accepts. Inputs are considered identical if they are === to each other.

// TODO: Complete this

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();

    return function() {

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