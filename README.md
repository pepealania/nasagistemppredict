# 🌡️ NASA Global Temperature Prediction Full-Stack App

A full-stack application that predicts NASA global temperature anomalies for a given year using a machine learning model.  
It consists of:  
- A Python script that loads a trained ML model and makes predictions.  
- A Node.js Express backend that calls the Python script and exposes an API.  
- A React frontend to input the year and display the predicted anomaly.

---

## 🚀 Tech Stack

- **Python 3** (ML model with scikit-learn and joblib)  
- **Node.js** with **Express** (backend API)  
- **python-shell** (Node.js to run Python scripts)  
- **React** (frontend UI)  

---

## 📂 Project Structure
project-root/
│
├── backend/
│ ├── predict.py # Python script to predict temperature anomaly
│ ├── temperature_model.pkl # Pre-trained ML model file
│ ├── server.js # Node.js Express API server
│ ├── package.json # Node.js dependencies
│ └── ... # Other backend files
│
├── frontend/
│ ├── src/
│ │ ├── App.js # React main app component
│ │ ├── index.js # React entry point
│ │ └── ... # Other React components
│ ├── package.json # React dependencies
│ └── ... # Other frontend files
│
└── README.md # This file


## 🔧 Setup Instructions

### Backend Setup

1. Navigate to the backend folder:

```bash
cd backend

2. Install Node.js dependencies:

npm install

3. Install Python dependencies:

pip install numpy scikit-learn joblib

4. Run the Node.js server (which will call Python scripts):

node server.js
The backend server will listen on port 5000 by default.

### Frontend Setup

1. Navigate to the frontend folder:

cd frontend

2. Install React dependencies:

npm install

3. Run the React development server:

npm start
This will open the React app in your browser, usually at http://localhost:3000.

🧠 How It Works

1. The React frontend sends a POST request to the Node.js backend /predict endpoint with a JSON body containing the year to predict.

2. The Node.js backend uses the python-shell package to run the Python predict.py script, passing the year as an argument.

3. The Python script loads the saved model (temperature_model.pkl), makes a prediction for the given year, and prints the result.

4. Node.js receives the prediction output and sends it back in the API response.

5. React displays the predicted temperature anomaly to the user.

🧪 API Endpoint

POST /predict

Request JSON body:
{
  "year": "2035"
}

Response JSON:
{
  "year": "2035",
  "predicted_anomaly": 1.3421
}

📜 Troubleshooting

1. Ensure Python and Node.js are installed and accessible from your terminal.

2. Make sure all required packages are installed (pip install for Python, npm install for Node and React).

3. In predict.py, use print(..., flush=True) so Node.js can receive output without delays.

4. Confirm the ML model file temperature_model.pkl is in the backend folder.

5. If the React app cannot reach the backend, check CORS settings and that both servers are running on correct ports.

📂 Sample React Component Snippet

Here’s a minimal example of how the React frontend might call the backend:

import React, { useState } from 'react';

function App() {
  const [year, setYear] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ year }),
    });
    const data = await res.json();
    setResult(data.predicted_anomaly);
  };

  return (
    <div>
      <h1>NASA Temperature Anomaly Predictor</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Enter year"
          value={year}
          onChange={(e) => setYear(e.target.value)}
          required
        />
        <button type="submit">Predict</button>
      </form>
      {result !== null && (
        <p>Predicted anomaly for {year}: {result.toFixed(4)}</p>
      )}
    </div>
  );
}

export default App;

📜 License
MIT License — Feel free to fork, modify, and use.

👤 Author
Jose Alania 

