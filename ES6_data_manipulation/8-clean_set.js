export default function cleanSet(set, str) {
  let resStr = '';
  set.forEach((x) => {
    if (x.slice(0, str.length) === str && str.length !== 0) {
      if (resStr.length !== 0) {
        resStr += '-';
      }
      resStr += x.slice(str.length);
    }
  });
  return resStr;
}
