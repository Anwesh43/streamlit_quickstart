import streamlit as st 
import pandas as pd 
import numpy as np 

df = pd.DataFrame({
    "a" : [10, 20, 30, 40],
    "b" : [15, 30, 45, 60],
    "c": [20, 40, 60, 80]
})

#st.write(df)
st.dataframe(df)

st.dataframe(df.sum())

st.dataframe(df.sum(axis=1))

st.dataframe(df.std())
st.dataframe({
    "sum_stack": [df.stack().sum()],
    "np_sum": [np.sum(df.values)]
})

st.dataframe(df.stack())