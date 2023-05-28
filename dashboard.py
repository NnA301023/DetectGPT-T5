# TODO: Implement Dashboard Visualisation
import streamlit as st 
from utils import read_logs


st.table(read_logs())