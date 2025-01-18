import streamlit as st 
import pandas as pd 

st.header("Display Data")
c1,c2,c3,c4 = st.columns(4)
obj = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
df = pd.DataFrame(obj)

with c1:
    st.subheader("Display dataframe")
    st.dataframe(df)
with c2:
    st.subheader("Display table")
    st.table(df)
with c3:
    st.subheader("Display json")
    st.json(obj)

with c4:
    st.subheader("Display metric")
    st.metric(label= "TATA Motors", value = 843, delta = 0.1)