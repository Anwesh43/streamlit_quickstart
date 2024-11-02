import streamlit as st 

_,c1, _ = st.columns([1, 3, 1])
_,c2,_ = st.columns([1, 3, 1])
_,c3,_ = st.columns([1, 3, 1])
imageUrl = "https://bit.ly/edus3ha"
videoUrl = "https://bit.ly/canibs3"
audioUrl = "https://bit.ly/rainaws3"

with c1:
    st.subheader("Image")
    st.image(imageUrl)

with c2:
    st.subheader("Video")
    st.video(videoUrl)

with c3:
    st.subheader("Audio")
    st.audio(audioUrl)