import streamlit as st
import fitz
import pickle
from rake_nltk import Rake
import re
import io 
from io import BytesIO


def load_functions():
    with open('text_extraction_and_keyword.pkl', 'rb') as file:
        loaded_extract_text = pickle.load(file)
        loaded_extract_keywords = pickle.load(file)
        loaded_cleaned_keywords = pickle.load(file)
    
    return loaded_extract_text, loaded_extract_keywords, loaded_cleaned_keywords

st.title("KEYWORD EXTRACTION FROM PDF FILE")

uploaded_file = st.file_uploader("UPLOAD A PDF FILE", type=["pdf"])

if uploaded_file is not None:
    # Use BytesIO to read the file content as bytes
    pdf_content = BytesIO(uploaded_file.read())
    
    # Load functions
    loaded_extract_text, loaded_extract_keywords, loaded_cleaned_keywords = load_functions()
    
    # Use loaded_extract_text function to extract text
    pdf_text = loaded_extract_text(pdf_content.read().decode('utf-8'))
    
    st.subheader("Extracted text")
    st.text(pdf_text)

    pdf_keywords = loaded_extract_keywords(pdf_text)
    cleaned_keywords = loaded_cleaned_keywords(pdf_keywords)

    st.subheader("Cleaned Keywords:")
    for score, keyword in cleaned_keywords:
        st.text(f"{score:.2f}: {keyword}")
