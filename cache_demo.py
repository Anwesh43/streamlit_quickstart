import streamlit as st 

defaultText : str = ""
result = 0
header = st.header("")
i = 0 
@st.cache_data  
def power(a : int, b : int) -> int:
    header = st.header("Evaluated from function {0}, {1}".format(a, b))
    return a ** b 

a = st.number_input("Enter number for a")
b = st.number_input("Enter number for b")

button = st.button("Multiply")

if button:
    result = power(a, b)
    st.header("Power of {0} to {1} is {2}".format(a, b, result))
   


   
