import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="StudentLife AI",
    page_icon="🎓",
    layout="wide"
)

# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

# Title
st.title("🎓 StudentLife AI")

st.subheader("AI-Powered Student Performance Analysis")

st.markdown("---")

# Welcome section
st.header("👋 Welcome to StudentLife AI")

st.write(
    """
    StudentLife AI is a student performance analysis system that
    combines Data Analytics and Machine Learning to analyze
    student academic information and predict final performance.
    """
)

# Project banner
st.info(
    "🤖 **Machine Learning + 📊 Data Analytics + 🎓 Student Performance**"
)

st.markdown("---")

# Dataset overview
st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍🎓 Students",
        len(data)
    )

with col2:
    st.metric(
        "📚 Features",
        len(data.columns)
    )

with col3:
    st.metric(
        "🎯 Average Final Grade",
        f"{data['G3'].mean():.1f} / 20"
    )

st.markdown("---")

# Features
st.header("🚀 Project Features")

col1, col2 = st.columns(2)

with col1:

    st.info(
        "📊 **Data Analytics**\n\n"
        "Analyze study time, absences and "
        "academic performance."
    )

    st.info(
        "🤖 **Machine Learning**\n\n"
        "Predict the student's final grade "
        "using a Random Forest model."
    )

with col2:

    st.info(
        "📈 **Visual Analytics**\n\n"
        "Explore charts showing relationships "
        "between student factors and grades."
    )

    st.info(
        "💡 **Performance Insights**\n\n"
        "View predicted performance, risk level "
        "and personalized suggestions."
    )

st.markdown("---")

# How it works
st.header("⚙️ How StudentLife AI Works")

st.write(
    """
    **1️⃣ Enter student details**

    **2️⃣ Analyze the student's academic data**

    **3️⃣ Machine Learning model processes the inputs**

    **4️⃣ Predicted final grade is generated**

    **5️⃣ Performance insights are displayed**
    """
)

st.markdown("---")

st.success(
    "🎓 Use the sidebar to explore all StudentLife AI features!"
)