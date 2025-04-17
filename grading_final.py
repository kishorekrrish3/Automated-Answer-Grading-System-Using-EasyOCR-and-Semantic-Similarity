import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image
from textblob import TextBlob
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from sentence_transformers import SentenceTransformer, util

# Load pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Correct spelling function
def correct_spelling(text_list):
    corrected_text = [" ".join([TextBlob(word).correct().string for word in sentence.split()]) for sentence in text_list]
    return corrected_text

# Calculate similarity and grading function
def calculate_similarity(extracted_text, answer_keys):
    # Step 1: Correct OCR spelling mistakes
    corrected_text = correct_spelling(extracted_text)

    # Step 2: Join the extracted text into one string
    student_answer = " ".join(corrected_text)

    # Step 3: Generate embeddings for both texts
    student_embedding = model.encode(student_answer, convert_to_tensor=True)
    
    best_score = 0
    best_feedback = ""
    for answer_key in answer_keys:
        answer_embedding = model.encode(answer_key, convert_to_tensor=True)

        # Step 4: Compute cosine similarity
        similarity_score = util.cos_sim(student_embedding, answer_embedding).item()
        
        # Provide feedback on the answer
        feedback = compare_sentences(student_answer, answer_key)
        
        # Check if this is the best similarity score
        if similarity_score > best_score:
            best_score = similarity_score
            best_feedback = feedback

    # Step 5: Compute marks (out of the total marks provided)
    marks_scored = round(best_score * 10, 2)  # Scale similarity score to 10 marks

    return {
        "corrected_student_answer": student_answer,
        "similarity_percentage": round(best_score * 100, 2),
        "marks_scored": marks_scored,
        "feedback": best_feedback
    }

# Compare sentences for answer-wise feedback
def compare_sentences(student_answer, answer_key):
    student_sentences = student_answer.split('. ')
    answer_sentences = answer_key.split('. ')
    
    feedback = []
    for student, answer in zip(student_sentences, answer_sentences):
        if student.lower().strip() == answer.lower().strip():
            feedback.append(f"Correct: {student}")
        else:
            feedback.append(f"Incorrect: {student} (Expected: {answer})")
    
    return "\n".join(feedback)

# OCR Reader setup
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=True)

reader = load_reader()

# Streamlit UI setup
st.title("📝 Automated Grading System using OCR")
st.markdown("Upload an answer sheet image. The system will extract the answer using OCR, correct spelling, and compare it with multiple model answers using semantic similarity.")

uploaded_file = st.file_uploader("📄 Upload Answer Sheet Image", type=["png", "jpg", "jpeg"])

# Model answer(s) input
answer_key_1 = st.text_area("✅ Enter Model Answer 1", height=150)
answer_key_2 = st.text_area("✅ Enter Model Answer 2 (optional)", height=150)
answer_key_3 = st.text_area("✅ Enter Model Answer 3 (optional)", height=150)

# List of provided model answers
answer_keys = [answer_key_1, answer_key_2, answer_key_3]

# File handling and OCR process
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # Convert image to numpy array for OCR
    image_np = np.array(image)

    with st.spinner("🔍 Extracting text with OCR..."):
        result = reader.readtext(image_np, detail=0)
    
    st.subheader("🗒️ Extracted Text:")
    st.write(result)

# Total marks input and evaluation
total_marks = st.number_input("🔢 Enter Total Marks for the Question", min_value=1, value=10)

# Button to trigger evaluation
if st.button("📊 Evaluate"):
    if answer_key_1 and total_marks > 0:
        with st.spinner("Calculating similarity and generating score..."):
            evaluation = calculate_similarity(result, answer_keys)

        st.markdown("## 📋 Results")
        st.write(f"**Corrected Student Answer:** {evaluation['corrected_student_answer']}")
        st.write(f"**Similarity Score:** {evaluation['similarity_percentage']}%")
        st.write(f"**Marks Scored (out of {total_marks}):** {evaluation['marks_scored']}")
        st.write("### Feedback:")
        st.write(evaluation['feedback'])
    else:
        st.error("Please enter a model answer and total marks before evaluating.")
