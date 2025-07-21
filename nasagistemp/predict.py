import sys
import joblib
import numpy as np
print("starting prediction...")
model = joblib.load("temperature_model.pkl")
year = int(sys.argv[1])
print(f"prediction for year {year}")
prediction = model.predict(np.array([[year]]))
print(prediction[0])