/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    const ar = [];
    for (const idx of array) {
        ar.push(appendString + idx);
    }
    return ar;
}
