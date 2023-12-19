# pdf_functions.py
import fitz
from rake_nltk import Rake
import re
from io import BytesIO

class PDFFunctions:
    @staticmethod
    def extract_text_from_pdf(pdf_content):
        doc = fitz.open(stream=pdf_content)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text("text.utf8").replace('\uFFFD', 't')
        return text

    @staticmethod
    def extract_keywords_from_text(text):
        r = Rake()
        r.extract_keywords_from_text(text)
        keywords = r.get_ranked_phrases_with_scores()
        return keywords

    @staticmethod
    def clean_keywords(keywords):
        cleaned_keywords = [(score, re.sub(r'[^a-zA-Z0-9\s]', '', phrase)) for score, phrase in keywords]
        return cleaned_keywords
