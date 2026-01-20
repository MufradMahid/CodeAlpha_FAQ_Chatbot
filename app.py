import streamlit as st
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- FAQ DATA ---------------- #
faqs = [
    {
        "question": "What is CodeAlpha internship?",
        "answer": "CodeAlpha internship is a program that provides practical experience in AI and software development."
    },
    {
        "question": "Is this internship paid?",
        "answer": "This internship is unpaid but provides certificates and learning experience."
    },
    {
        "question": "How long is the internship?",
        "answer": "The internship duration is typically one month."
    },
    {
        "question": "Will I get a certificate?",
        "answer": "Yes, you will receive a completion certificate after successful submission."
    },
    {
        "question": "How do I submit my tasks?",
        "answer": "You need to submit your completed tasks using the submission form provided by CodeAlpha."
    }
]

# ---------------- SIMPLE PREPROCESSING (NO NLTK) ---------------- #
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

questions = [preprocess(faq["question"]) for faq in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

# ---------------- CHATBOT FUNCTION ---------------- #
def chatbot_response(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, question_vectors)
    index = similarity.argmax()
    return faqs[index]["answer"]

# ---------------- STREAMLIT UI ---------------- #
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to the internship.")

user_input = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = chatbot_response(user_input)
        st.success(response)
