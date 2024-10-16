const assert = require('assert');
const calculateNumber = require('./0-calcul.js')

describe('calculateNumber()', () => {
  it('should return a sum of the rounded integers', () => {
    assert.equal(calculateNumber(1.6, 3.2), 5);
  })
});
