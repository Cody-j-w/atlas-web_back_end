export default function createInt8TypedArray(len, pos, val) {
  const newBuffer = new ArrayBuffer(len);
  if (pos >= len) {
    throw new Error("Position outside range");
  }
  let bufferView = new DataView(newBuffer);
  bufferView.setInt8(pos, val);
  return bufferView;
}
