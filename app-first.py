import streamlit as st
import pandas as pd

st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application.")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to the app.")

# create a sample DataFrame
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})
st.dataframe(data)