import streamlit as st

# MBTI에 따른 직업 추천과 잘 맞는 사람의 성향 데이터
mbti_info = {
    "ISTJ": {"job": "장부관리자, 건축가, 계획가",
             "match": "차분한 사람, 능력적이고 지적인 사람"},
    "ISFJ": {"job": "과학자, 간호사, 유치원 교사",
             "match": "노력하고 신중한 방식의 사람"},
    "INFJ": {"job": "치료사, 컨설턴트, 만화가",
             "match": "희망적이고 가치 지향적인 사람"},
    "INTJ": {"job": "공학자, 디자이너, 전략기획자",
             "match": "도움을 받고 복원이 빠른 사람"},
    "ISTP": {"job": "기술 관련 전문가, 파일럿, 엔지니어",
             "match": "건강하고 현실적이며 의지가 강한 사람"},
    "ISFP": {"job": "영화 제작자, 조각가, 예술가",
             "match": "감성적이고 진정한 사람"},
    "INFP": {"job": "작가, 상담사, 치료사",
             "match": "다른 사람의 개별성을 존중하며 열정적인 사람"},
    "INTP": {"job": "연구원, 데이터 분석가, 회계 전문가",
             "match": "논리적으로 말하며 균형 잡힌 사고를 하는 사람"},
}

# 스트림릿 제목
st.title("\U0001F4C2 MBTI에 따른 직업과 잘 맞는 성향 추천")

# 드롭다운 메뉴 MBTI 선택
options = list(mbti_info.keys())
selected_mbti = st.selectbox("\U0001F50D 당신의 MBTI를 선택해주세요!", options)

# 선택한 MBTI의 정보 표시
if selected_mbti:
    st.subheader(f"\U0001F389 {selected_mbti} 유형 추천 직업 및 성향")
    st.write(f"\U0001F4BC **추천 직업:** {mbti_info[selected_mbti]['job']}")
    st.write(f"\U0001F91D **잘 맞는 사람 성향:** {mbti_info[selected_mbti]['match']}")

# 앱 하단 메시지
st.info("\U0001F680 MBTI 유형에 맞는 직업을 참고하여 나만의 계획을 세워보세요!")
