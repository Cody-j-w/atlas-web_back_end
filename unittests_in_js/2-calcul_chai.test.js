const chai = require('chai');
const calculateNumber = require('./1-calcul.js')

expect = chai.expect;

describe('calculateNumber()', () => {
  it('should return a sum of rounded a and rounded b', () => {
    expect(calculateNumber('SUM', 1.6, 3.2)).to.equal(5);
    expect(calculateNumber('SUM', 1.3, 5)).to.equal(6);
    expect(calculateNumber('SUM', 2, 4.7)).to.equal(7);
  });
  it('should return rounded a divided by rounded b', () => {
    expect(calculateNumber('DIVIDE', 2, 1.4)).to.equal(2);
    expect(calculateNumber('DIVIDE', 5.4, 10)).to.equal(0.5);
    expect(calculateNumber('DIVIDE', 9.2, 2.7)).to.equal(3);
    expect(calculateNumber('DIVIDE', 123.456, 0)).to.equal('Error');
  });
  it('should return rounded a minus rounded b', () => {
    expect(calculateNumber('SUBTRACT', 5, 2.2)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 5.4, 2)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 5.6, 2.6)).to.equal(3);
  });
});
