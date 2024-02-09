require('dotenv').config();

const cors = require('cors');
const express = require('express');
const app = express();

app.use(express.json());
app.use(cors());

app.post('/api/v1/data', (req, res) => {
    res.send('Hello');
});

const port = process.env.PORT || 3000;

const start = () => {
    try {
        app.listen(port, () => {
            console.log(`Server is listening on port ${port}`);
        })
    } catch (error) {
        console.log(`Error: ${error}`);
    }
}

start();