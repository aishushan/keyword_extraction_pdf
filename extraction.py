# extraction.py
import pdf_functions
import streamlit as st
import fitz
import pickle
from rake_nltk import Rake
import re
import io 
from io import BytesIO
#from pdf_functions import PDFFunctions
#from .pdf_functions import PDFFunctions
from pdf_functions import PDFFunctions

st.title("KEYWORD EXTRACTION FROM PDF FILE")

# File upload section
uploaded_file = st.file_uploader("UPLOAD A PDF FILE", type=["pdf"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Instantiate the PDFFunctions class
    pdf_functions_instance = PDFFunctions()

    # Use BytesIO to read the file content as bytes
    pdf_content = BytesIO(uploaded_file.read())

    # Use the methods of the PDFFunctions class
    pdf_text = pdf_functions_instance.extract_text_from_pdf(pdf_content)

    # Display the extracted text
    st.subheader("Extracted text")
    st.text(pdf_text)

    # Extract keywords and clean them
    pdf_keywords = pdf_functions_instance.extract_keywords_from_text(pdf_text)
    cleaned_keywords = pdf_functions_instance.clean_keywords(pdf_keywords)

    # Display cleaned keywords
    st.subheader("Cleaned Keywords:")
    for score, keyword in cleaned_keywords:
        st.text(f"{score:.2f}: {keyword}")

