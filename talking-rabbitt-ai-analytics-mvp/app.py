import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt - Conversational Analytics")

uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:
        if "highest revenue" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()
            top_region = result.idxmax()

            st.write(f"Region with highest revenue: {top_region}")

            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)
            st.pyplot(fig)