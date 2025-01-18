import streamlit as st 

pages = [
    'display_button.py',
    'display_progress.py',
    'display_select.py',
    'display_charts.py',
    'display_expander.py',
]
for page in pages:
    button = st.button("Navigate to {0}".format(page.replace(".py", "")))
    if button:
        st.switch_page("pages/{0}".format(page))