import sys
import joblib
import pandas as pd
print("starting prediction...")
model = joblib.load("temperature_model.pkl")
year = int(sys.argv[1])
X_input = pd.DataFrame({'Year': [year]})
print(f"prediction for year {year}")
prediction = model.predict(X_input)[0]
print(prediction)