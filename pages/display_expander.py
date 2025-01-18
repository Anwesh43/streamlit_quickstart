import streamlit as st 
import numpy as np 
data = np.random.randn(5, 5)
with st.expander("Display Bar Chart"):
    button = st.button("Randomize data")
    bar_chart = st.bar_chart(data)
    if button:
        data = np.random.rand(5, 5)
