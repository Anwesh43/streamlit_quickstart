import streamlit as st 

number = st.sidebar.slider("Enter value", min_value = 1, max_value = 100)

st.header("Number is {0}".format(number))