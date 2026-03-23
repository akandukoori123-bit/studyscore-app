#!/usr/bin/env python3
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

print("\n📚 StudyScore Predictor (CLI)\n")

try:
    hours_studied = float(input("Hours studied (0-12): "))
    hours_sleep = float(input("Hours of sleep (0-12): "))
    practice_problems = float(input("Practice problems (0-50): "))
    confidence_level = float(input("Confidence level (1-10): "))
    days_before_test = float(input("Days before test (0-14): "))
    
    # Validate ranges
    hours_studied = max(0, min(12, hours_studied))
    hours_sleep = max(0, min(12, hours_sleep))
    practice_problems = max(0, min(50, practice_problems))
    confidence_level = max(1, min(10, confidence_level))
    days_before_test = max(0, min(14, days_before_test))
    
    # Predict
    features = np.array([[hours_studied, hours_sleep, practice_problems, confidence_level, days_before_test]])
    prediction = model.predict(features)[0]
    prediction = max(0, min(100, prediction))
    
    print(f"\n✅ Predicted Score: {prediction:.1f}/100\n")
    
    if prediction >= 90:
        print("🌟 Excellent — you look very well prepared!")
    elif prediction >= 80:
        print("💪 Strong — you're in a good position.")
    elif prediction >= 70:
        print("📖 Solid — a little more prep could help.")
    elif prediction >= 60:
        print("⚠️  You're on the edge — more studying needed.")
    else:
        print("❌ You may want a stronger study plan.")
        
except ValueError:
    print("❌ Invalid input. Please enter numbers.")
