export default class Currency {
    constructor(code, name) {
      this._code = code;
      this._name = name;
    }
  
    set code(scode) {
      if (typeof scode !== 'string') {
        throw TypeError('Code must be a string');
      }
      this._code = scode;
    }
  
    get code() {
      return this._code;
    }
  
    set name(sname) {
      if (typeof sname !== 'string') {
        throw TypeError('Name must be a string');
      }
      this._name = sname;
    }
  
    get name() {
      return this._name;
    }
  
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
}
