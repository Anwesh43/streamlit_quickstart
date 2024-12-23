import streamlit as st 
import pandas as pd 
file = st.file_uploader("Upload a file", type = ["jpg", "png"])

if file is not None:
    st.image(file)

df = pd.DataFrame({
    "Mamal": ["Dog", "Cat", "Mouse"],
    "Number": [4, 5, 1]
})

button = st.download_button("Download csv", df.to_csv(index=False),file_name = 'data.csv')
