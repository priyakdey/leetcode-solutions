// 2622. Cache With Time Limit
//
// Write a class that allows getting and setting key-value pairs, however a time
// until expiration is associated with each key.
//
// The class has three public methods:
// - set(key, value, duration): accepts an integer key, an integer value, and a
//   duration in milliseconds. Once the duration has elapsed, the key should be inaccessible.
//   The method should return true if the same un-expired key already exists and
//   false otherwise. Both the value and duration should be overwritten if the key already exists.
// - get(key): if an un-expired key exists, it should return the associated value.
//   Otherwise it should return -1.
// - count(): returns the count of un-expired keys.

var Value = function(value, timeoutId) {
    this.value = value;
    this.timeoutId = timeoutId;
};

var TimeLimitedCache = function() {
    this.table = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let isKeyPresent = false;

    if (this.table.has(key)) {
        clearTimeout(this.table.get(key).timeoutId);
        this.table.delete(key);
        isKeyPresent = true;
    }

    this.table.set(key, new Value(value, -1));
    const timeoutId = setTimeout(() => this.table.delete(key), duration);
    this.table.get(key).timeoutId = timeoutId;

    return isKeyPresent;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.table.has(key)) {
        return this.table.get(key).value;
    }

    return -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.table.size;
};