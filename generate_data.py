import pandas as pd
import random

rows = []

for _ in range(200):
    hours_studied = random.randint(0, 12)
    hours_sleep = random.randint(4, 10)
    practice_problems = random.randint(0, 50)
    confidence_level = random.randint(1, 10)
    days_before_test = random.randint(0, 14)

    # Build a semi-realistic score
    score = (
        35
        + hours_studied * 3.0
        + hours_sleep * 1.5
        + practice_problems * 0.6
        + confidence_level * 1.2
        + days_before_test * 0.8
    )

    # Add some randomness so it feels more realistic
    score += random.randint(-10, 10)

    # Keep score in a normal range
    score = max(0, min(100, round(score)))

    rows.append([
        hours_studied,
        hours_sleep,
        practice_problems,
        confidence_level,
        days_before_test,
        score
    ])

df = pd.DataFrame(rows, columns=[
    "hours_studied",
    "hours_sleep",
    "practice_problems",
    "confidence_level",
    "days_before_test",
    "score"
])

df.to_csv("student_habits.csv", index=False)
print("Generated student_habits.csv with 200 rows.")