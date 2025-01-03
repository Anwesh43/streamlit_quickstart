import streamlit as st 

increment = st.button("Increment +")
decrement = st.button("Decrement -")
counter = 0 
delta = 0 
if "counter" in st.session_state:
    counter = st.session_state["counter"]
else:
    st.session_state["counter"] = 0 

if increment:
    counter = st.session_state["counter"] + 1
    st.session_state["counter"] = counter 
    delta = 1

if decrement:
    counter = st.session_state["counter"] - 1 
    st.session_state["counter"] = counter 
    delta = -1

st.caption(st.session_state["counter"])
st.metric("Temperature {0}".format(counter), delta)