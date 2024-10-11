import streamlit as st
from word_count import count_word_frequencies

st.title('Word Frequency Count App')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file:
    with open('temp.txt','wb') as f:
        f.write(uploaded_file.getbuffer())

word_frequencies = count_word_frequencies('temp.txt')

st.write('Word Frequencies: ')
st.write(word_frequencies)