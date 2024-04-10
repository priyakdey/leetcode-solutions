// 2631. Group By
//
// Write code that enhances all arrays such that you can call the
// array.groupBy(fn) method on any array and it will return a grouped
// version of the array.
//
// A grouped array is an object where each key is the output of fn(arr[i]) and
// each value is an array containing all items in the original array with that key.
//
// The provided callback fn will accept an item in the array and return a
// string key.
//
// The order of each value list should be the order the items appear in the
// array. Any order of keys is acceptable.
//
// Please solve it without lodash's _.groupBy function.

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, curr) => {
        const key = fn(curr);

        if (!acc[key]) {
            acc[key] = [];
        }

        acc[key].push(curr);
        return acc;
    }, {});
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */