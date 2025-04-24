import asyncio
import sys

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
import easyocr
import cv2
import numpy as np
import re
from PIL import Image
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import wordninja

# Load models
@st.cache_resource
def load_models():
    return {
        'embedding_model': SentenceTransformer('all-MiniLM-L6-v2'),
        'spell_checker': pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base"),
        'grammar_checker': pipeline("text2text-generation", model="pszemraj/flan-t5-large-grammar-synthesis")
    }

models = load_models()

# Advanced text cleaning and correction
def enhance_ocr_text(raw_text_list):
    raw_text = " ".join(raw_text_list)
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s\.,\?!\-\'\"]', ' ', raw_text)
    cleaned_text = re.sub(r'_', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    split_words = []
    for word in cleaned_text.split():
        if len(word) > 10 or any(c.isdigit() for c in word):
            split_words.extend(wordninja.split(word))
        else:
            split_words.append(word)
    joined_text = " ".join(split_words)
    
    corrected_spelling = models['spell_checker'](
        joined_text,
        max_length=1024,
        num_beams=5,
        repetition_penalty=2.5,
        early_stopping=True
    )[0]['generated_text']
    
    enhanced_text = models['grammar_checker'](
        f"Fix grammatical errors in this text: {corrected_spelling}",
        max_length=1024,
        num_beams=5,
        repetition_penalty=2.5,
        early_stopping=True
    )[0]['generated_text']
    
    enhanced_text = re.sub(r'\s+([.,!?])', r'\1', enhanced_text)
    return enhanced_text

def calculate_similarity(extracted_text, answer_keys, total_marks):
    student_answer = enhance_ocr_text(extracted_text)
    student_embedding = models['embedding_model'].encode(student_answer, convert_to_tensor=True)
    
    best_score = 0
    best_feedback = ""
    for answer_key in answer_keys:
        if not answer_key.strip():
            continue
            
        answer_embedding = models['embedding_model'].encode(answer_key, convert_to_tensor=True)
        similarity_score = util.cos_sim(student_embedding, answer_embedding).item()
        
        feedback = compare_sentences(student_answer, answer_key)
        
        if similarity_score > best_score:
            best_score = similarity_score
            best_feedback = feedback

    marks_scored = round(best_score * total_marks, 2)
    return {
        "corrected_student_answer": student_answer,
        "similarity_percentage": round(best_score * 100, 2),
        "marks_scored": marks_scored,
        "feedback": best_feedback
    }

def compare_sentences(student_answer, answer_key):
    student_sentences = student_answer.split('. ')
    answer_sentences = answer_key.split('. ')
    
    feedback = []
    for i, (student, answer) in enumerate(zip(student_sentences, answer_sentences)):
        student = student.strip()
        answer = answer.strip()
        if not student or not answer:
            continue
            
        if student.lower() == answer.lower():
            feedback.append(f"✅ Sentence {i+1}: Correct")
        else:
            feedback.append(f"❌ Sentence {i+1}:\nStudent: {student}\nExpected: {answer}")
    
    return "\n\n".join(feedback)

@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=True)

reader = load_reader()

# Streamlit UI
st.title("📝 AI-Powered Automated Grading System")
st.markdown("""
This enhanced system:
1. Uses advanced OCR text cleaning
2. Implements NLP-powered spelling/grammar correction
3. Compares answers using semantic similarity
""")

uploaded_file = st.file_uploader("📄 Upload Answer Sheet Image", type=["png", "jpg", "jpeg"])

answer_key_1 = st.text_area("✅ Enter Model Answer 1 (Required)", height=150)
answer_key_2 = st.text_area("📝 Enter Model Answer 2 (Optional)", height=150)
answer_key_3 = st.text_area("📝 Enter Model Answer 3 (Optional)", height=150)
answer_keys = [ak for ak in [answer_key_1, answer_key_2, answer_key_3] if ak.strip()]

result = []
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Fixed image preprocessing
    image_np = np.array(image)
    if len(image_np.shape) == 3:  # Color image
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    else:  # Grayscale
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_GRAY2BGR)

    enhanced_color = cv2.detailEnhance(image_bgr, sigma_s=10, sigma_r=0.15)
    gray = cv2.cvtColor(enhanced_color, cv2.COLOR_BGR2GRAY)
    
    with st.spinner("🔍 Performing advanced text extraction..."):
        result = reader.readtext(gray, detail=0, paragraph=True)
    
    st.subheader("Raw OCR Output:")
    st.write(result)

total_marks = st.number_input("🔢 Enter Total Marks for the Question", 
                             min_value=1, value=10, step=1)

if st.button("📊 Evaluate Answer"):
    if not answer_keys:
        st.error("Please provide at least one model answer")
    elif total_marks <= 0:
        st.error("Total marks must be a positive number")
    else:
        with st.spinner("🧠 Processing text and evaluating..."):
            evaluation = calculate_similarity(result, answer_keys, total_marks)
            
        st.markdown("## 📋 Evaluation Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Similarity Score", f"{evaluation['similarity_percentage']}%")
        with col2:
            st.metric("Marks Awarded", f"{evaluation['marks_scored']}/{total_marks}")
            
        st.markdown("### 🧹 Cleaned Student Answer")
        st.write(evaluation['corrected_student_answer'])
        
        st.markdown("### 📝 Detailed Feedback")
        st.write(evaluation['feedback'])
