const http = require('http');
const studentsf = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = await studentsf(process.argv[2]);
      res.end(data);
    } catch (err) {
      res.end(err.message);
    }
    res.end();
  }
}).listen(1245);

module.exports = app;