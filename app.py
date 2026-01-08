import streamlit as st
import pickle
import re

# Load the saved models and vectorizer
with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('regressor.pkl', 'rb') as f:
    reg = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

def clean_text(text):
    text = re.sub(r'\\$.*?\\$', ' MATH_EXPRESSION ', text)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return " ".join(text.split())

# Web UI Layout
st.title("⚖️ AutoJudge: Problem Difficulty Predictor")
st.markdown("Paste the problem details below to predict its difficulty.")

desc = st.text_area("Problem Description")
in_desc = st.text_area("Input Description")
out_desc = st.text_area("Output Description")

if st.button("Predict Difficulty"):
    if desc and in_desc and out_desc:
        # 1. Preprocess
        combined = desc + " " + in_desc + " " + out_desc
        cleaned = clean_text(combined)
        
        # 2. Transform
        features = tfidf.transform([cleaned])
        
        # 3. Predict
        prob_class = clf.predict(features)[0]
        prob_score = reg.predict(features)[0]
        
        # 4. Display Results
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Predicted Class", prob_class)
        with col2:
            st.metric("Predicted Score", f"{prob_score:.2f}")
    else:
        st.error("Please fill in all three text boxes.")