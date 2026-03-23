import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("student_habits.csv")

X = df[["hours_studied", "hours_sleep", "practice_problems", "confidence_level", "days_before_test"]]
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("Model trained and saved!")
