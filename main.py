import streamlit as st

# MBTI에 따른 직업 추천과 잘 맞는 사람의 성향 데이터 mbti_info = {
    "ISTJ": {"job": "🔢 장마부, 건모가, 계획가",
              "match": "🙂 천천한 사람, 능력적이고 지력적인 사람"},
    "ISFJ": {"job": "🏥 과학서 자무가, 건모가, 유\ce58원",
              "match": "🤟 노력하고 막간한 방식의 사람"},
    "INFJ": {"job": "🌟 치유고용가, 커·체재업가, 만화가",
              "match": "🧐 희망적이고 가치구원적인 사람"},
    "INTJ": {"job": "🤖 공학자, 디자인 만들기, 체질과수",
              "match": "🤟 도움을 받고 복원이 빠른 사람"},
    "ISTP": {"job": "⚙️ 기술에 가지가 있는 업공가, 수류에사",
              "match": "⚡️ 건강하고 대상적이며 반심이 약하는 사람"},
    "ISFP": {"job": "🌟 영화 만들기, 공장가, 예술가",
              "match": "🌟 결성적이고 진정한 사람"},
    "INFP": {"job": "🎨 만화가, 작가, 치료자",
              "match": "🤗 동아의 개별성을 중심으로 열심해는 사람"},
    "INTP": {"job": "🔬 연구자, 신화력 에사, 회계전문가",
              "match": "💡 천사를 말하며 예상 바가지의 인생과 조화"},
}

# 스트림릿 제목 st.title("\U0001F4C2 MBTI 어느 직업과 이상이 작단할까? ")

# 드롭다운 메뉴 MBTI 선택 options = list(mbti_info.keys())
selected_mbti = st.selectbox("\U0001F50D 만제의 MBTI를 선택해주세요!", options)

# 선택한 MBTI의 정보 표시 if selected_mbti:
    st.subheader(f"\U0001F389 {selected_mbti} 만제의 반대")
    st.write(f"\U0001F4BC **\uac1c본적 강점:** {mbti_info[selected_mbti]['job']}")
    st.write(f"\U0001F91D **\uac00지가 잘 맞는 사람:** {mbti_info[selected_mbti]['match']}")

# 앱 하단 메세지 st.info("\ud83d\ude80 MBTI 선택에 따라 고려할 직업을 위한 계획을 세워보세요!")
