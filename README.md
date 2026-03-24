# StudyScore Predictor

StudyScore is a simple machine learning web app that predicts a student's quiz score based on study habits such as study time, sleep, practice problems, confidence, and preparation time.

---

## Overview

This project demonstrates a full machine learning pipeline:

- Data generation (synthetic dataset)  
- Model training using scikit-learn  
- Deployment as an interactive web app using Streamlit  

The model learns patterns from student habits and predicts a score out of 100 for new inputs.

---

## How It Works

1. A dataset of student habits is generated using `generate_data.py`  
2. `train_model.py` trains a machine learning model on this dataset  
3. The trained model is saved as `model.pkl`  
4. `app.py` loads the model and provides an interactive UI for predictions  

---

## Features Used

The model uses the following inputs:

- Hours studied  
- Hours of sleep  
- Practice problems completed  
- Confidence level (1–10)  
- Days before the test started studying  

Output:
- Predicted score (0–100)

---

## Model

This project uses a RandomForestRegressor.

- It builds multiple decision trees using conditions like:
  - "Is hours_studied > 4?"
  - "Is sleep < 6?"
- Each tree makes a prediction  
- The final prediction is the average of all trees  

---

## Tech Stack

- Python  
- pandas  
- scikit-learn  
- Streamlit  
- NumPy  

---

## How to Run Locally

1. Clone the repository: 
```
git clone https://github.com/your-username/studyscore-app.git 
cd studyscore-app
```
2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Generate the dataset:
```
python generate_data.py
```
5. Train the model:
```
python train_model.py
```
6. Run the app:
```
streamlit run app.py
```

---

## Example Use

Adjust the sliders in the app to simulate different study habits and observe how they affect predicted performance.

---

## Disclaimer

This project uses synthetic data and is intended for educational and demonstration purposes only. It is not a real predictive model of student performance.

---

## Future Improvements

- Use real-world datasets  
- Add data visualizations (graphs)  
- Improve model accuracy  
- Deploy online (Streamlit Cloud / Render)  
- Add user login and history tracking  

---

## Author

Aditya Kandukoori