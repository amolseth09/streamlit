import streamlit as st
import pandas as pd

st.title("Core components & layouts")
st.markdown("This is **bold text** , this is *itealic text* and this is a [link](https://streamlit.io).")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

subscribe = st.checkbox("Subscribe to newsletter")

if st.button("Submit"):
    st.write(f"Name: {name}, Age: {age}, Subscribed: {subscribe}")

color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue", "Yellow"])
st.write(f"Your favorite color is: {color}")

# split page into two columns
col1, col2 = st.columns(2)
with col1:
    st.write("column 1: slider example")
    slider_value = st.slider("Select a value:", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")
with col2:
    st.write("Column 2: Radio button example")
    choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {choice}")

# create a sample DataFrame
data = pd.DataFrame({
    "Fruit": ["Apple", "Banana", "Cherry"],
    "Quantity": [10, 20, 15]
})

# Display static dataframe/table
st.table(data)