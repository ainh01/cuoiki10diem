require('http').createServer((req, res) => {
  res.end(req.url === '/health' ? 'OK' : 'Not Found');
}).listen(3000, () => console.log('Running on :3000'));
