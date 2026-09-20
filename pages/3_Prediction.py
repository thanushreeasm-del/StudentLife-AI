import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

st.title("🤖 StudentLife AI - Prediction")

st.write("Enter student details to predict the final grade.")

# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# Features
features = ["studytime", "absences", "G1", "G2"]

X = data[features]
y = data["G3"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Model evaluation
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Model performance
st.header("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", f"{r2:.2f}")

with col2:
    st.metric("Mean Absolute Error", f"{mae:.2f}")

st.markdown("---")

# Student inputs
st.header("📚 Enter Student Details")

studytime = st.number_input(
    "📖 Study Time",
    min_value=1,
    max_value=4,
    value=2
)

absences = st.number_input(
    "🚫 Number of Absences",
    min_value=0,
    max_value=75,
    value=5
)

G1 = st.number_input(
    "📝 First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

G2 = st.number_input(
    "📝 Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)

# Prediction
if st.button("🔮 Predict Final Grade"):

    student = pd.DataFrame({
        "studytime": [studytime],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    prediction = model.predict(student)[0]

    prediction = max(0, min(20, prediction))

    st.markdown("---")

    st.header("🎯 Prediction Result")

    st.success(
        f"Predicted Final Grade: {prediction:.1f} / 20"
    )

    # Grade progress
    st.subheader("📊 Grade Progress")

    percentage = (prediction / 20) * 100

    st.progress(percentage / 100)

    st.write(
        f"📈 Overall Score: **{percentage:.1f}%**"
    )

    # Performance level
    if prediction >= 16:
        st.info("🌟 Performance Level: Excellent")

    elif prediction >= 12:
        st.info("👍 Performance Level: Good")

    elif prediction >= 10:
        st.info("🙂 Performance Level: Average")

    else:
        st.warning("⚠️ Performance Level: Needs Improvement")

    # Risk level
    st.subheader("🚦 Student Risk Level")

    if prediction >= 12:
        st.success(
            "🟢 Low Risk — Student is performing well."
        )

    elif prediction >= 10:
        st.warning(
            "🟡 Medium Risk — Student may need some improvement."
        )

    else:
        st.error(
            "🔴 High Risk — Student may need additional support."
        )

    # Student summary
    st.subheader("📋 Student Performance Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📖 Study Time", studytime)

    with col2:
        st.metric("🚫 Absences", absences)

    with col3:
        st.metric("📝 G1", G1)

    with col4:
        st.metric("📝 G2", G2)

    # Suggestions
    st.subheader("💡 Personalized Suggestions")

    suggestions = []

    if studytime <= 1:
        suggestions.append(
            "📚 Try to spend more time studying regularly."
        )

    if absences >= 10:
        suggestions.append(
            "🏫 Try to reduce absences and attend classes regularly."
        )

    if G1 < 10:
        suggestions.append(
            "📝 Focus on improving your first-period performance."
        )

    if G2 < 10:
        suggestions.append(
            "📝 Try to improve your second-period performance."
        )

    if not suggestions:
        suggestions.append(
            "🌟 Good academic habits! Keep maintaining your current routine."
        )

    for suggestion in suggestions:
        st.write(suggestion)

# Feature importance
st.markdown("---")

st.header("⭐ Feature Importance")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

st.bar_chart(
    importance.set_index("Feature")
)
