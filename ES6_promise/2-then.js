export default function handleResponseFromAPI(promise) {
    promise.then(() => {
        return {
            status: 200,
            body: 'Success'
        }
    }).then(() => {
        console.log("Got a response from the API");
    }).catch(() => {
        return new Error();
    })
}