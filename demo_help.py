import streamlit as st 

dropdown = st.selectbox("Select a method to show help text", options = ["add", "sub"]) 
def addNum(a, b):
    """
        I add two numbers 
    """
    return a + b 

def subNum():
    """
     I sub two nums
    """
    return a - b

map = {
    "add": addNum,
    "sub": subNum,
}
if dropdown:
    st.help(map[dropdown])
