import streamlit as st 

name = st.text_input("Please enter name")
st.header("Your name is {0}".format(name))

num1 = st.number_input("Please enter 1st number", min_value = 1, max_value = 100)


num2 = st.number_input("Please enter 2nd number", min_value = 1, max_value = 100)

st.header("Sum of two numbers {0}".format(num1 + num2))