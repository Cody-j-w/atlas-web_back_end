const getPaymentTokenFromApi = require('./6-payment_token.js');
const { expect, assert } = require('chai');

describe('getPaymentTokenFromApi()', () => {
    it('should return {data: "Successful response from the API" } when successful', (done) => {
        getPaymentTokenFromApi(true)
        .then((data) => {
            assert.equal("{data: 'Successful response from the API' }", data);
            done();
        });
    });
});