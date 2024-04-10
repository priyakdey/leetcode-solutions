// 2677. Chunk Array

// Given an array arr and a chunk size size, return a chunked array.
// A chunked array contains the original elements in arr, but consists of subarrays
// each of length size. The length of the last subarray may be less than size if
// arr.length is not evenly divisible by size.
//
// You may assume the array is the output of JSON.parse.
// In other words, it is valid JSON.
//
// Please solve it without using lodash's _.chunk function.

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const length = arr.length;
    const chunkCount =
        Math.floor(arr.length / size) + (arr.length % size !== 0 ? 1 : 0);
    const chunks = new Array(chunkCount);

    let cursor = 0;

    for (let i = 0; i < chunkCount; i++) {
        chunks[i] = arr.slice(cursor, Math.min(cursor + size, length));
        cursor = cursor + size;
    }

    return chunks;
};