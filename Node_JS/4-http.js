const http = require('http');

const server = http.createServer((req, res) => {
  res.write('Hello Holberton School!');
  res.end();
});

server.listen(1245, () => {
  console.log('listing on 1245!');
});
