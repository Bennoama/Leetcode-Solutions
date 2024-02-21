// https://leetcode.com/problems/calculator-with-method-chaining

class Calculator {
  
  /** 
   * @param {number} value
   */
  constructor(value) {
      this.number = value;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  add(value){
      this.number += value;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  subtract(value){
      this.number -= value;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */  
  multiply(value) {
      this.number *= value;
  }

  /** 
   * @param {number} value
   * @return {Calculator}
   */
  divide(value) {
      if (0 == value) {
          throw "Division by zero is not allowed";
      }
      this.number /= value;
  }
  
  /** 
   * @param {number} value
   * @return {Calculator}
   */
  power(value) {
      this.number = Math.pow(this.number, value);
  }
    
  /** 
   * @return {number}
   */
  getResult() {
      return this.number;
  }
}