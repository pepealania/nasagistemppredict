import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [year, setYear] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handlePredict = async () => {
    try {
      const res = await axios.post('http://localhost:5000/predict', { year });
      setPrediction(res.data.predicted_anomaly.toFixed(3));
    } catch (err) {
      alert("Error fetching prediction");
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>🌍 NASA Global Temperature Predictor</h1>
      <input
        type="number"
        value={year}
        onChange={(e) => setYear(e.target.value)}
        placeholder="Enter a year (e.g., 2035)"
      />
      <button onClick={handlePredict}>Predict</button>
      {prediction && (
        <p>Predicted Temperature Anomaly for {year}: {prediction} °C</p>
      )}
    </div>
  );
}

export default App;