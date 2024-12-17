import streamlit as st
import pandas as pd
import random

# Load periodic table data
file_path = "periodic_table_113_elements.csv"
data = pd.read_csv(file_path)

# Function to generate quiz questions
def generate_quiz(data, num_questions=10):
    questions = []
    elements = data.sample(n=num_questions).to_dict(orient='records')
    for elem in elements:
        question = {
            "question": f"What is the symbol of the element '{elem['Name']}' (Atomic Number: {elem['Atomic Number']})?",
            "answer": elem['Symbol']
        }
        questions.append(question)
    return questions

# Streamlit App
st.title("Periodic Table Quiz")
st.write("Test your knowledge of the elements in the periodic table!")

# Generate questions
num_questions = 10
quiz_questions = generate_quiz(data, num_questions)

# Quiz Interaction
score = 0
user_answers = []

st.write("### Quiz: Enter your answers below")
for i, q in enumerate(quiz_questions):
    user_input = st.text_input(f"{i+1}. {q['question']}", key=f"question_{i}")
    user_answers.append((q['answer'], user_input))

# Submit and evaluate
if st.button("Submit Quiz"):
    score = sum(1 for correct, user in user_answers if correct.lower() == user.strip().lower())
    st.write(f"## Your Score: {score}/{num_questions}")
    st.write("### Correct Answers:")
    for i, (correct, user) in enumerate(user_answers):
        st.write(f"{i+1}. Correct Answer: {correct} | Your Answer: {user if user else 'No answer'}")

st.write("Good luck and keep practicing!")

