const getPaymentTokenFromApi = require('./6-payment_token.js');
const { expect } = require('chai');

describe('getPaymentTokenFromApi()', () => {
    it('should return {data: "Successful response from the API" } when successful', (done) => {
        getPaymentTokenFromApi(true)
        .then((data) => {
            if (data) {
                done();
            }
        });
    });
    it('should fail this test', (done) => {
        getPaymentTokenFromApi(false)
        .then((data) => {
            if (data) {
                done();
            }
        });
    })
});