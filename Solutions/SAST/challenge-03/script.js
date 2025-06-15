const { spawn } = require('child_process');

function run(cmd, args) {
  const child = spawn(cmd, args, { stdio: 'inherit' });
  child.on('error', err => console.error(err));
}
