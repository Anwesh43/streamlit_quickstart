import streamlit as st 

select = st.selectbox("Which country do you live in", ["India", "US", "UK", "Canada"])

text = st.header("You live in {0}".format(select))

radio = st.radio("Do you belive in God?" , ["Yes", "No"])

radioTextMap = {
    "Yes": "I beleive in God",
    "No": "I don't believe"
}
st.header(radioTextMap[radio])

select_slider = st.select_slider("Which country do you live in", ["India", "US", "UK", "Canada"])

st.caption(select_slider)

slider = st.slider(min_value = 0, max_value = 100, value = 25, label = "Choose Value")

st.markdown("Value is {0}".format(slider))