import streamlit as st 

with st.form("Details Form"):
    country = st.selectbox("Country", ["India", "USA", "UK", "Norway"])
    name = st.text_input("Enter your name")
    gender = st.radio("Your Gender?", ["Male", "Female"])
    submit_button = st.form_submit_button("Submit Form")
    if submit_button:
        st.header("Country: {0}, Name: {1}, gender {2}".format(country, name, gender))
    