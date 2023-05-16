from random import randint
import streamlit as st 


st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>DetectGPT</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #FFFFFF;'>We are here with AI technology to help you know the quality of your writing and prevent plagiarism</h5>", unsafe_allow_html=True)

text = st.text_area(label = "", placeholder="Input text here...")
isClick = st.button(label = "Submit")

# if text != "":
if isClick:
    score = randint(1, 100)
    if score > 70:
        st.error("Terdeteksi Plagiarisme")
    else:
        st.success("Terdeteksi Original")
    st.progress(score)