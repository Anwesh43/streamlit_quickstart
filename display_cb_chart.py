import streamlit as st 
import numpy as np 
chart = st.empty()

data = np.random.randn(5, 5)
if st.checkbox("Display chart"):
    chart = st.bar_chart(data)
else:
    chart.empty()

if st.button("Load new data"):
    data = np.random.randn(5, 5)