// 2725. Interval Cancellation
//
// Given a function fn, an array of arguments args, and an interval time t, 
// return a cancel function cancelFn.
//
// After a delay of cancelTimeMs, the returned cancel function cancelFn 
// will be invoked.
//
// setTimeout(cancelFn, cancelTimeMs)
// The function fn should be called with args immediately and then called again 
// every t milliseconds until cancelFn is called at cancelTimeMs ms.

/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
    fn(...args);
    // the fn function will be run every t ms
    const intervalId = setInterval(() => fn(...args), t);

    // handler to cancel the fn function after cancelTimeInMs ms.
    return function (cancelTimeInMs) {
        setTimeout(() => clearInterval(intervalId), cancelTimeInMs);
    }

};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 2;
 *  const args = [4], t = 35, cancelTimeMs = 190;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  setTimeout(cancel, cancelTimeMs);
 *   
 *  setTimeout(() => {
 *      console.log(result); // [
 *                           //     {"time":0,"returned":8},
 *                           //     {"time":35,"returned":8},
 *                           //     {"time":70,"returned":8},
 *                           //     {"time":105,"returned":8},
 *                           //     {"time":140,"returned":8},
 *                           //     {"time":175,"returned":8}
 *                           // ]
 *  }, cancelTimeMs + t + 15)    
 */