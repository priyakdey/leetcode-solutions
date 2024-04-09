// 2703. Return Length of Arguments Passed
//
// Write a function argumentsLength that returns the count of arguments 
// passed to it.

/**
 * @return {number}
 */
var argumentsLength = function (...args) {
  return args?.length ?? 0;
};