// 2723. Add Two Promises
//
// Given two promises promise1 and promise2, return a new promise. 
// promise1 and promise2 will both resolve with a number. 
// The returned promise should resolve with the sum of the two numbers.

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
  let value1 = await promise1;
  let value2 = await promise2;
  return value1 + value2;
};