// 2628. JSON Deep Equal
// 
// Given two values o1 and o2, return a boolean value indicating whether two values, 
// o1 and o2, are deeply equal.
// 
// For two values to be deeply equal, the following conditions must be met:
// - If both values are primitive types, they are deeply equal if they pass 
//   the === equality check.
// - If both values are arrays, they are deeply equal if they have the same 
//   elements in the same order, and each element is also deeply equal according 
// to these conditions.
// - If both values are objects, they are deeply equal if they have the same keys, 
//   and the associated values for each key are also deeply equal according to 
//   these conditions.
// 
// You may assume both values are the output of JSON.parse. 
// In other words, they are valid JSON.
// 
// Please solve it without using lodash's _.isEqual() function

/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function (o1, o2) {
    if (o1 === o2) return true;
    if (o1 === null || o2 === null) return false;
    if (String(o1) !== String(o2)) return false;

    if (typeof o1 !== 'object') {
        return o1 === o2;
    }

    if (Array.isArray(o1)) {
        if (o1.length !== o2.length) return false;

        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) return false;
        }

        return true;
    }

    if (Object.keys(o1).length !== Object.keys(o2).length) return false;

    for (const key in o1) {
        if (!areDeeplyEqual(o1[key], o2[key])) return false;
    }

    return true;
};