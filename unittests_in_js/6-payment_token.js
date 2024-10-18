async function getPaymentTokenFromApi(token) {
    if (token === true) {
        return Promise.resolve({data: 'Successful response from the API' });
    }
}

module.exports = getPaymentTokenFromApi;