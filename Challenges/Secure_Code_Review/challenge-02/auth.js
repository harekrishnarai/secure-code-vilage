const crypto = require('crypto');

function generateToken() {
  const rand = Math.random().toString(36);
  return crypto.createHash('sha1').update(rand).digest('hex');
}
