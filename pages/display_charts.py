import streamlit as st 
import numpy as np 

data = np.random.randn(5, 5)
print(data)

c1,_ = st.columns([3, 1])
c2,_ = st.columns([3, 1])
c3,_ = st.columns([3, 1])
print(c1)
with c1:
    st.subheader("Line Chart")
    st.line_chart(data)

with c2:
    st.subheader("Area Chart")
    st.area_chart(data)

with c3:
    st.subheader("Bar Chart")
    st.bar_chart(data)
