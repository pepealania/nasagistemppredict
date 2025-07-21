const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');

const app = express();
const PORT = 5000;
app.use(cors());
//app.use(bodyParser.json());
app.use(express.json()); 

app.post('/predict', (req, res) => {
    console.log(`body is: ${JSON.stringify(req.body, null, 2)}`);
    const { year } = req.body;
    console.log(`year is : ${year}`);

  const options = {
    scriptPath: __dirname,
    pythonOptions: ['-u'], 
    args: [year.toString()]
  };

  console.log("Calling PythonShell...");

  PythonShell.run('predict.py', options, (err, results) => {
    if (err) {
      console.error("PythonShell error:", err);
      return res.status(500).json({ error: 'Prediction failed', details: err.message });
    }

    console.log("PythonShell results:", results);

    if (!results || results.length === 0) {
        return res.status(500).json({ error: 'No result returned from Python script' });
    }    

    return res.json({
      year,
      predicted_anomaly: parseFloat(results[0])
    });
  });
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));