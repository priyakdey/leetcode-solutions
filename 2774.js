// 2774. Array Upper Bound
// 
// Write code that enhances all arrays such that you can call the upperBound() 
// method on any array and it will return the last index of a given target number. 
// 
// nums is a sorted ascending array of numbers that may contain duplicates. 
// If the target number is not found in the array, return -1.

/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let index = -1;
    let left = 0,
        right = this.length - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        if (this[mid] === target) {
            index = mid;
            left = mid + 1;
        } else if (this[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return index;
};


// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5