import streamlit as st
import docx2txt
from PyPDF2 import PdfReader
from transformers import pipeline

# Initialize the pipeline with the AI detection model
detector = pipeline('text-classification', model='akshayvkt/detect-ai-text')
    
def check_if_ai_generated(text):
    results = detector(text)
    # Extract the score and convert it to a percentage
    score = results[0]['score'] * 100 if results[0]['label'] == 'AI' else (1 - results[0]['score']) * 100
    return round(score, 2)

# Streamlit interface
st.title("AI Text Detection")
input_text = st.text_area("Enter text to check:")
if st.button("Analyze"):
    if input_text:
        score = check_if_ai_generated(input_text)
        st.write(f"AI-generated likelihood: {score}%")
    else:
        st.write("Please enter some text to analyze.")


