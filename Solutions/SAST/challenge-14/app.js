const express = require('express');
const { execFile } = require('child_process');
const app = express();

app.get('/run', (req, res) => {
    execFile('/usr/bin/safe_script.sh', [req.query.arg || ''], (err, stdout) => {
        if (err) return res.status(500).send('error');
        res.send(stdout);
    });
});

app.listen(3000);
