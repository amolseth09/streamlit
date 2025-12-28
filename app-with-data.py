import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Workling with data in streamlit")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

# clean the data

if uploaded_file is not None:
    if st.checkbox("Show missing value counts"):
        st.write(df.isnull().sum())
    if st.checkbox("Drop rows with missing values"):
        df = df.dropna()
        st.write("Cleaned Data Preview:")
        st.dataframe(df.head())

if uploaded_file is not None:
    st.subheader("Quick Statistics")
    st.write(df.describe())

# Choose a column for Visualization
if uploaded_file is not None:
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    if numeric_columns:
        selected_col = st.selectbox("Choose a numeric column for visualization", numeric_columns)
        # Create histogram
        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"Histogram of {selected_col}")
        # Render in Streamlit
        st.pyplot(fig)