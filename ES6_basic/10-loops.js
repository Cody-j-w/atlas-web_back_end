export default function appendToEachArrayValue(array, appendString) {
  let newArr = [];
  for (const idx of array) {
    const value = idx;
    const newVal = appendString + value;
    newArr.push(newVal);
  }

  return newArr;
}
