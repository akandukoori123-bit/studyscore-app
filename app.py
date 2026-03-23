import streamlit as st
import joblib
import numpy as np
import warnings

# Suppress sklearn warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Page settings
st.set_page_config(page_title="StudyScore Predictor", page_icon="📚")

# Load trained model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# Title and intro
st.title("📚 StudyScore Predictor")
st.write(
    "This app predicts a quiz score based on study habits like study time, sleep, "
    "practice problems, confidence, and how early you started preparing."
)

st.divider()

# User inputs
st.subheader("Enter Study Habits")

hours_studied = st.slider("Hours studied", min_value=0, max_value=12, value=4)
hours_sleep = st.slider("Hours of sleep", min_value=0, max_value=12, value=7)
practice_problems = st.slider("Practice problems completed", min_value=0, max_value=50, value=15)
confidence_level = st.slider("Confidence level (1-10)", min_value=1, max_value=10, value=5)
days_before_test = st.slider("Days before the test you started studying", min_value=0, max_value=14, value=3)

st.divider()

# Predict button
if st.button("Predict Score"):
    features = np.array([[
        hours_studied,
        hours_sleep,
        practice_problems,
        confidence_level,
        days_before_test
    ]])

    prediction = model.predict(features)[0]
    prediction = max(0, min(100, prediction))  # keep it between 0 and 100

    st.subheader(f"Predicted Score: {prediction:.1f}")

    # Feedback message
    if prediction >= 90:
        st.success("Excellent — you look very well prepared for the quiz.")
    elif prediction >= 80:
        st.success("Strong — you're in a good position.")
    elif prediction >= 70:
        st.info("Solid — a little more prep could raise your score.")
    elif prediction >= 60:
        st.warning("You're on the edge — more studying and practice would help.")
    else:
        st.error("You may want a stronger study plan before the quiz.")

    # Extra advice
    st.subheader("Quick Advice")

    advice = []

    if hours_studied < 4:
        advice.append("- Try increasing your study time.")
    if hours_sleep < 6:
        advice.append("- More sleep could help your performance.")
    if practice_problems < 15:
        advice.append("- Doing more practice problems may improve your score.")
    if confidence_level < 5:
        advice.append("- Build confidence by reviewing easier problems first.")
    if days_before_test < 2:
        advice.append("- Starting earlier usually leads to better results.")

    if advice:
        for tip in advice:
            st.write(tip)
    else:
        st.write("Your habits look pretty strong overall.")

# Footer
st.divider()
st.caption("Built with Streamlit, Python, and scikit-learn.")