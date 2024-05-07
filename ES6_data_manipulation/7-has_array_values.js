export default function hasValuesFromArray(set, arr) {
  for (let i = 0; i < arr.length; i++) {
    if (set.has(arr[i]) === false) {
      return false;
    }
  }
  return true;
}
