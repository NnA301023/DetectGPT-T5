import streamlit as st
from utils import read_logs
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

if __name__ == "__main__":

    st.title("Dasboard DetectGPT")

    data = read_logs()
    col_1, col_2 = st.columns(2)

    with col_1:
        st.subheader("Score Distribution")
        temp_df = data[['timestamp', 'score']]
        temp_df = temp_df.rename(columns = {"timestamp" : "index"}).set_index('index')
        st.line_chart(temp_df, height = 455)

    with col_2:
        st.subheader("Text Frequency")
        list_free_text = " ".join(data['text_input'].tolist())
        wordcloud = WordCloud(background_color = "white", max_words = 50)
        wordcloud.generate(list_free_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation = "bilinear")
        ax.axis("off")
        st.pyplot(fig)