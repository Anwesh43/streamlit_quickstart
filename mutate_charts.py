import streamlit as st 
import pandas as pd 
import numpy as np 
df1 = pd.DataFrame({
    "Cats": np.random.randn(5),
    "Dogs": np.random.randn(5)
})

df2 = pd.DataFrame({
    "Cats": np.random.randn(5),
    "Dogs": np.random.randn(5)
 })

line_chart = st.line_chart(df1)

button = st.button("Add data in chart")

if button:
    line_chart.add_rows(df2)
    df2 = pd.DataFrame({
        "Cats": np.random.randn(5),
        "Dogs": np.random.randn(5)
    })


