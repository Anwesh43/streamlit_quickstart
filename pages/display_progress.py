import streamlit as st 
import time 

st.markdown("### st.warning()")
st.warning("This will be deprecated soon")

st.markdown("### st.info()")
st.info("App running optimally")
with st.spinner('Counting...'):
    progress_bar = st.progress(0)
    for d in range(100):
        progress_bar.progress(d)
        time.sleep(0.1)
    st.success("Done loading")
    
st.balloons()