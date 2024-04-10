// 2722. Join Two Arrays by ID

// Given two arrays arr1 and arr2, return a new array joinedArray. All the objects 
// in each of the two inputs arrays will contain an id field that has an integer 
// value. joinedArray is an array formed by merging arr1 and arr2 based on their 
// id key. The length of joinedArray should be the length of unique values of id. 
// The returned array should be sorted in ascending order based on the id key.
// 
// If a given id exists in one array but not the other, the single object with 
// that id should be included in the result array without modification.
// 
// If two objects share an id, their properties should be merged into a single
// object:
// 
// - If a key only exists in one object, that single key-value pair should be 
//   included in the object.
// - If a key is included in both objects, the value in the object from arr2 
//   should override the value from arr1.

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();

    for (let item of arr1) {
        map.set(item.id, item);
    }

    for (let item of arr2) {
        let id = item.id;
        if (map.has(id)) {
            map.set(id, {
                ...map.get(id),
                ...item
            });
        } else {
            map.set(id, item);
        }
    }

    const mergedArr = new Array(map.size);
    let cursor = 0;
    for (let item of map.values()) {
        mergedArr[cursor++] = item;
    }

    mergedArr.sort((obj1, obj2) => {
        if (obj1.id < obj2.id) {
            return -1;
        } else if (obj1.id === obj2.id) {
            return 0;
        } else {
            return 1;
        }
    });

    return mergedArr;
};