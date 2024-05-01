import streamlit as st 
import pandas as pd 
import numpy as np 

df = pd.DataFrame({
    "a" : [10, 20, 30, 40],
    "b" : [15, 30, 45, 60],
    "c": [20, 40, 60, 80]
})

#st.write(df)
st.write("DataFrame")
st.dataframe(df)
st.write("DataFrame sum")
st.dataframe(df.sum())
st.write("DataFrame sum axis = 1")
st.dataframe(df.sum(axis=1))
st.write("DataFrame std deviation")
st.dataframe(df.std())
st.dataframe({
    "sum_stack": [df.stack().sum()],
    "np_sum": [np.sum(df.values)]
})

st.write("df stack")
st.dataframe(df.stack())
st.write("df minimum")
st.dataframe(df.min())
st.write("df max")
st.dataframe(df.max())

st.write("df count")
st.dataframe(df.count())

df1 = pd.DataFrame({
    "a": [1, 2],
    "b": [3, 4]
})

st.write("Df1")
st.dataframe(df1)

df2 = pd.DataFrame({
    "b": [8, 9],
    "c": [6, 7]
})
st.write("df2")
st.dataframe(df2)

df3 = pd.concat([df1, df2], join="inner")
st.write("df3")
st.dataframe(df3)