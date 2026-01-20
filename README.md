# CodeAlpha_FAQ_Chatbot
This project is an FAQ chatbot developed for Task 2 of the CodeAlpha Internship. It uses Natural Language Processing with TF-IDF and cosine similarity to match user questions with predefined FAQs and display accurate answers through a simple and interactive Streamlit web interface.
# 🤖 FAQ Chatbot using NLP and Streamlit

This project is developed as **Task 2** for the **CodeAlpha Internship Program**.

## 📌 Project Description
The FAQ Chatbot is an AI-based application that answers frequently asked questions using
Natural Language Processing techniques. It matches user queries with predefined FAQs
and returns the most relevant answer.

## 🛠️ Technologies Used
- Python
- Streamlit
- Scikit-learn (TF-IDF & Cosine Similarity)

## ⚙️ How It Works
1. User enters a question through the Streamlit interface.
2. The text is preprocessed (lowercasing and punctuation removal).
3. TF-IDF vectorization converts text into numerical form.
4. Cosine similarity finds the closest matching FAQ.
5. The chatbot displays the most relevant answer.

## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

🤖 What Kind of Chatbot Is This?

Type: Rule-based + NLP-based FAQ Chatbot

Not a generative AI chatbot

Works by matching similarity, not by generating new text

Best suited for customer support, help desks, and information systems
