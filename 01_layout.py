import streamlit as st

st.title("Understanding App Layouts (Columns & Expanders) Images")
st.sidebar.header("Apply Text")
text = st.sidebar.text_area("Here")
button1 = st.sidebar.button("What Features I have learned")
button2 = st.sidebar.button("Which features are next")
if button1: 
    st.write(text)
if button2: 
    st.write(text)


if button1: 
    col1, col2 = st.columns(2)
    col1_expander = st.expander("Expand Orginal")
    col1.header("What features I have already learned")
    col1.text("text")

    col2.header("Which features I still need to learn")
    col2.text("text")
   

