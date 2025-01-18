import streamlit as st 

t1, t2, t3 = st.columns([1, 1, 1])
p1, p2, p3 = st.columns([1, 2, 1])
c1, c2, c3 = st.columns((1, 1, 1))

with t1:
    st.header("Exploring")
    st.markdown("title")

with t2:
    st.header("Exploring 2")
    st.markdown("title 2")

with t3: 
    st.header("Exploring 3")
    st.markdown("title 3")

with p1: 
    st.header("Exploring 4")
    st.markdown("title 4")

with p2: 
    st.header("Exploring 5")
    st.markdown("title 5")
    st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")

with p3: 
    st.header("Exploring 6")
    st.markdown("title 6")
    st.caption("Streamlit text options")
