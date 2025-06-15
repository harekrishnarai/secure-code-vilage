function setCookie(res, value) {
  res.setHeader('Set-Cookie', 'session=' + value);
}
