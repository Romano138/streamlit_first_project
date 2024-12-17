import streamlit as st
import pandas as pd
import random

# Load periodic table data
file_path = "periodic_table_113_elements.csv"
data = pd.read_csv(file_path)

# Function to generate quiz questions (Simplified for Middle School Level)
def generate_quiz(data, num_questions=3):
    questions = []
    elements = data.sample(n=num_questions).to_dict(orient='records')
    for elem in elements:
        question = {
            "question": f"원소 '{elem['Name']}'의 기호는 무엇일까요? (원자 번호: {elem['Atomic Number']})",
            "answer": elem['Symbol']
        }
        questions.append(question)
    return questions

# Streamlit App
st.title("주기율표 퀴즈")
st.write("주기율표 원소에 대한 지식을 확인해보세요! (중학생 수준)")

# Generate questions
num_questions = 3
quiz_questions = generate_quiz(data, num_questions)

# Quiz Interaction
score = 0
user_answers = []

st.write("### 퀴즈: 아래에 답을 입력하세요")
for i, q in enumerate(quiz_questions):
    user_input = st.text_input(f"{i+1}. {q['question']}", key=f"question_{i}")
    user_answers.append((q['answer'], user_input))

# Submit and evaluate
if st.button("퀴즈 제출하기"):
    score = sum(1 for correct, user in user_answers if correct.lower() == user.strip().lower())
    st.write(f"## 당신의 점수: {score}/{num_questions}")
    st.write("### 정답 확인:")
    for i, (correct, user) in enumerate(user_answers):
        st.write(f"{i+1}. 정답: {correct} | 당신의 답: {user if user else '답 없음'}")

st.write("화이팅! 계속 연습해보세요!")
