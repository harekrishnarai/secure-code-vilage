const { exec } = require('child_process');

function run(cmd) {
  exec(cmd, (err, out) => {
    if (err) { console.error(err); return; }
    console.log(out);
  });
}
