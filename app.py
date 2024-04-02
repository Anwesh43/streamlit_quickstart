import streamlit as st 
import pandas as pd 

df = pd.DataFrame({
    "a" : [10, 20, 30, 40],
    "b" : [15, 30, 45, 60],
    "c": [20, 40, 60, 80]
})

#st.write(df)
st.dataframe(df)
