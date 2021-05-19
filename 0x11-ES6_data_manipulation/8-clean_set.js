const cleanSet = (set, startString) => {
  let str = '';
  if (startString && typeof startString === 'string') {
    set.forEach((i) => {
      if (i.startsWith(startString)) {
        str += `${i.slice(startString.length)}-`;
      }
    });
    return str.slice(0, str.length - 1);
  }
  return str;
};

export default cleanSet;
