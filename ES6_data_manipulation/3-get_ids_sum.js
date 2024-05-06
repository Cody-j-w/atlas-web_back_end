export default function getStudentsIdsSum(arr) {
  const initialValue = 0;
  return arr.reduce((accumulator, currentValue) => accumulator + currentValue.id, initialValue);
}
