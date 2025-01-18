import streamlit as st 
import time 


if st.button("progress"):
    
    pb = st.progress(0)
    for d in range(101):
        time.sleep(0.05)
        pb.progress(d)
    pb.empty()
    success = st.success("Done")
    time.sleep(3)
    success.empty()