import os
import streamlit as st 
from random import randint
from utils import create_table, logs


st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>DetectGPT</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #FFFFFF;'>We are here with AI technology to help you know the quality of your writing and prevent plagiarism</h5>", unsafe_allow_html=True)

text = st.text_area(label = "", placeholder="Input text here...")
isClick = st.button(label = "Submit")

if isClick:
    score = randint(1, 100)
    if score > 70:
        st.error("Terdeteksi Plagiarisme")
    else:
        st.success("Terdeteksi Original")
    
    if os.listdir("database").__len__() == 0:
        create_table()
    logs(text, score)
    st.progress(score)