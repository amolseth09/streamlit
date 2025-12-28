import streamlit as st
import requests

# Access secret key

api_key = st.secrets["API_KEY"]

st.title("Secure API Access Demo")

url = "https://api.example.com/data"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    st.write("API Response:")
    st.json(response.json())
else:
    st.write(f"Failed to fetch data. Status code: {response.status_code}")