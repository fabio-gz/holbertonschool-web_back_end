const createInt8TypedArray = (length, position, value) => {
  if (position > length) throw new RangeError('Position outside range');
  const abuffer = new ArrayBuffer(length);
  const dataview = new DataView(abuffer);
  dataview.setUint8(position, value);
  return dataview;
};

export default createInt8TypedArray;
