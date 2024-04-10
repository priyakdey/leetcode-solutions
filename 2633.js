// 2633. Convert Object to JSON String
//
// Given a value, return a valid JSON string of that value. The value can be a
// string, number, array, object, boolean, or null. The returned string should not
// include extra spaces. The order of keys should be the same as the order returned
// by Object.keys().
//
// Please solve it without using the built-in JSON.stringify method.

/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return "null";
    }

    const buffer = [];

    if (Array.isArray(object)) {
        buffer.push("[");
        object.forEach((element, idx, arr) => {
            buffer.push(jsonStringify(element));

            if (idx < arr.length - 1) {
                buffer.push(",");
            }
        });
        buffer.push("]");
    } else if (typeof object === "string") {
        buffer.push(`"${object}"`);
    } else if (typeof object === "number" || typeof object === "boolean") {
        buffer.push(object);
    } else {
        buffer.push("{");
        Object.keys(object)
            .forEach((key, idx, arr) => {
                buffer.push(`"${key}":`)
                buffer.push(jsonStringify(object[key]));

                if (idx < arr.length - 1) {
                    buffer.push(",");
                }
            });
        buffer.push("}");
    }

    return buffer.join("");
};