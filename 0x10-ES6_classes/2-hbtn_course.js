export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(sname) {
    if (typeof sname !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = sname;
  }

  get name() {
    return this._name;
  }

  set length(slen) {
    if (typeof slen !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = slen;
  }

  get length() {
    return this._length;
  }

  set students(sstudents) {
    if (!Array.isArray(sstudents) && sstudents.every((e) => typeof e !== 'string')) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = sstudents;
  }

  get students() {
    return this._students;
  }
}
