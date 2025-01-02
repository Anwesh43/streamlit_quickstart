import streamlit as st 
import time 



def createPlaceHolder():
    placeholder = st.empty()
    placeholder.markdown("Sleeping for 2 seconds")
    time.sleep(2)
    placeholder.caption("Slept and woke up now")

def showCaptionOnClick():
    placeholder = st.empty()
    button = placeholder.button("Click")
    if button:
        placeholder.caption("Text")
        time.sleep(2)
        input = placeholder.text_input("Enter name")
        # time.sleep(2)
        st.caption(input)

with st.empty():
    for i in range(0, 5):
        st.markdown("Count {}".format(i + 1))
        time.sleep(1)
    st.markdown("Stopping counter")

showCaptionOnClick()
createPlaceHolder()
