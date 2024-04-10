// 2705. Compact Object
// 
// Given an object or array obj, return a compact object. A compact object is the 
// same as the original object, except with keys containing falsy values removed. 
// This operation applies to the object and any nested objects. 
// Arrays are considered objects where the indices are keys. 
// A value is considered falsy when Boolean(value) returns false.
// 
// You may assume the obj is the output of JSON.parse. In other words, it is 
// valid JSON.

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (typeof obj !== "object" || object === null) {
        return obj;
    }

    if (Array.isArray(obj)) {
        return obj.filter(e => e).map(e => compactObject(e));
    }

    const compactObj = {};

    for (const key in obj) {
        const value = obj[key];
        if (value) {
            compactObj[key] = typeof value === 'object' ? compactObject(value) : value;
        }
    }
    return compactObj;
};