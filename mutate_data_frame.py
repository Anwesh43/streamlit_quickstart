import streamlit as st 
import pandas as pd 

df1 = pd.DataFrame({
    "Animal": ["Dog", "Cat"],
    "Bird": ["Sparrow", "Parrot"],
    "Flower": ["Rose", "Tulip"]
})

st1 = st.dataframe(df1)

df2 = pd.DataFrame({
    "Animal": ["Tiger", "Lion"],
    "Bird": ["Pigeon", "Crow"],
    "Flower": ["Lotus", "Sunflower"]
})
st2 = st.dataframe(df2)

st3 = st.dataframe(df1)
st3.add_rows(df2)
