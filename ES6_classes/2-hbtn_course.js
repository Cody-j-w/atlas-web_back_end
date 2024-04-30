export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(val) {
    if (typeof (val) === 'string') {
      this._name = val;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set length(val) {
    if (typeof (val) === 'number') {
      this._length = val;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get length() {
    return this._length;
  }

  set students(arr) {
    if (Array.isArray(arr)) {
      this._students = arr;
    }
  }

  get students() {
    return this._students;
  }
}
