// 2757. Generate Circular Array Values
// 
// Given a circular array arr and an integer startIndex, return a generator object 
// gen that yields values from arr. The first time gen.next() is called on the 
// generator, it should should yield arr[startIndex]. 
// Each subsequent time gen.next() is called, an integer jump will be passed 
// into the function (Ex: gen.next(-3)).
// 
// - If jump is positive, the index should increase by that value, however if the 
//   current index is the last index, it should instead jump to the first index.
// - If jump is negative, the index should decrease by the magnitude of that value, 
//   however if the current index is the first index, it should instead jump to the 
//   last index.

/**
 * @param {Array<number>} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function* (arr, startIndex) {
    const length = arr.length;
    let index = startIndex % length;

    while (true) {
        const jump = yield arr[index];
        index = (index + jump) % length;
        if (index < 0) {
            index = length + index;
        }
    }

};