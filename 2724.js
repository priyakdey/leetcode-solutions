// 2724. Sort By
// Given an array arr and a function fn, return a sorted array sortedArr. 
// You can assume fn only returns numbers and those numbers determine the sort 
// order of sortedArr. sortedArray must be sorted in ascending order by fn output.
// 
// You may assume that fn will never duplicate numbers for a given array.

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  const compareFn = (a, b) => {
    const aValue = fn(a), bValue = fn(b);
    if (aValue === bValue) {
      return 0;
    }
    else if (aValue <= bValue) {
      return -1;
    }
    else {
      return 1;
    }
  }

  arr.sort(compareFn);
  return arr;
};
