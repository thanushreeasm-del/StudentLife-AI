import streamlit as st

st.title("🎓 About StudentLife AI")

st.header("📌 Project Overview")

st.write(
    """
    StudentLife AI is an AI-powered student performance analysis
    system developed using Data Analytics and Machine Learning.

    The system analyzes student academic information and predicts
    the student's final grade using a Machine Learning model.
    """
)

st.markdown("---")

st.header("🎯 Project Objectives")

st.write(
    """
    • Analyze student academic data

    • Study the relationship between study time, absences and grades

    • Predict the student's final grade

    • Identify student performance and risk levels

    • Provide personalized suggestions for improvement
    """
)

st.markdown("---")

st.header("🛠️ Technologies Used")

st.write(
    """
    🐍 Python

    📊 Pandas

    📈 Streamlit

    🤖 Scikit-learn

    🌳 Random Forest Machine Learning

    📁 UCI Student Performance Dataset
    """
)

st.markdown("---")

st.header("⚙️ How the System Works")

st.write(
    """
    1️⃣ Student data is collected.

    2️⃣ The data is analyzed using Data Analytics.

    3️⃣ Important student features are given to the Machine Learning model.

    4️⃣ The Random Forest model predicts the final grade.

    5️⃣ The system displays the prediction, risk level and suggestions.
    """
)

st.markdown("---")

st.success(
    "🎓 StudentLife AI combines Data Analytics and Machine Learning "
    "to support student performance analysis."
)
