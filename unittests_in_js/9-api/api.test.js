request = require('request');
const { expect, assert } = require('chai');

describe('Payment API index', () => {
    it('should return a successful status code and the landing message', () => {
        axios.get('localhost:7865/').then((res) => {
            assert.equal(res.status, 200);
            assert.equal(res.data, 'Welcome to the payment system');
        });
    });
});

describe('Payment API cart', () => {
    it('should return a successful status code with a valid id', () => {
        request('localhost:7865/cart/12', (error, response, body) => {
            assert.equal(response.statusCode, 200);
            assert.equal(body, 'Payment methods for cart 12');
        });
    });
    it('should return a 404 status with an invalid id', () => {
        axios.get('localhost:7865/cart/twelve', (error, response, body) => {
            assert.equal(response.statusCode, 404);
            assert.equal(body, 'Not found');
        })
    })
});