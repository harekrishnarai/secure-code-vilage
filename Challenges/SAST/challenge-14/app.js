const express = require('express');
const app = express();

app.get('/run', (req, res) => {
    const output = eval(req.query.cmd);
    res.send(String(output));
});

app.listen(3000);
