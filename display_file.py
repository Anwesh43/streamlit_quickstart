import streamlit as st 

file = st.file_uploader("Upload a file", type = ["jpg", "png"])

if file is not None:
    st.image(file)