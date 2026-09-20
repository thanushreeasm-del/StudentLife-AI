import streamlit as st
import pandas as pd

st.title("📊 StudentLife AI - Overview")

# Load UCI dataset
data = pd.read_csv("data/student-mat.csv", sep=";")

st.success("Real student dataset loaded successfully! ✅")

st.header("📋 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(data))

with col2:
    st.metric("Total Features", len(data.columns))

with col3:
    st.metric("Average Final Grade", f"{data['G3'].mean():.1f} / 20")

st.subheader("📚 Student Dataset")

st.dataframe(data)
