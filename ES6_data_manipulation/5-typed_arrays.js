export default function createInt8TypedArray(len, pos, val) {
  const newBuffer = new ArrayBuffer(len);
  new DataView(newBuffer).setInt8(pos, val);
  return newBuffer;
}
