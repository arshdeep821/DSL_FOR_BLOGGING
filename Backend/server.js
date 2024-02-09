require('dotenv').config();

const { StatusCodes } = require('http-status-codes');

const cors = require('cors');
const express = require('express');
const app = express();

app.use(express.json());
app.use(cors());

app.post('/api/v1/data', (req, res) => {
    tokens = req.body;
    console.log(tokens);
    eval(tokens);
    res.status(StatusCodes.CREATED).send('Web Site Created');
});

const port = process.env.PORT || 3000;

const start = () => {
    try {
        app.listen(port, () => {
            console.log(`Server is listening on port ${port} ...`);
        });
    } catch (error) {
        console.log(`Error: ${error}`);
    }
}

start();