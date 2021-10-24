import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.title('S14345: English to German simple translator')
# title

st.header('How to use')
# header

st.write('Choose translate option and next enter the text you want to translate in the field below. That is all!')
# text

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Options",
    [
        "English to German",
        "German to English",
    ],
)

if option == "English to German":
    text = st.text_area(label="Enter text")
    if text:
        classifier = pipeline("translation_en_to_de")
        answer = classifier(text)
        st.success('Translation done :)')
        st.write(answer[0]['translation_text'])
else:
    st.error('Yet not supported...')


st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
