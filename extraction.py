import streamlit as st
import fitz
import pickle 
from rake_nltk import Rake 
import re

with open('text_extraction_and_keyword.pkl','rb') as file:
    loaded_extract_text=pickle.load(file)
    loaded_extract_keywords=pickle.load(file)
    loaded_cleaned_keywords=pickle.load(file)
    
st.title("KEYWORD EXTRACTION FROM PDF FILE")

uploaded_file=st.file_uploader("UPLOAD A PDF FILE", type=["pdf"])

if uploaded_file is not None:
    pdf_text=loaded_extract_text(uploaded_text)
    st.subheader("extracted text")
    st.text(pdf_text)
    
    pdf_keywords=loaded_extract_keywords(pdf_text)
    cleaned_keywords=loaded_cleaned_keywords(pdf_keywords)
    
    st.subheader("cleaned_keywords:")
    for score, keyword in cleaned_keywords:
        st.text(f"{score:.2f}: {keyword}")