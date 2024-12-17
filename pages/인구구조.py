import streamlit as st
import pandas as pd

# Plotly 예외 처리
try:
    import plotly.express as px
except ModuleNotFoundError:
    st.error("Plotly 라이브러리가 설치되지 않았습니다. 'pip install plotly'를 실행해주세요.")
    st.stop()

# 데이터 불러오기
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# 최고/최저 비율 찾기 함수
def find_max_min_ratio(df, selected_region):
    region_data = df[df['행정구역'] == selected_region]
    ratios = region_data.iloc[:, 4:].T  # 연령별 인구수만 선택
    ratios.columns = ['인구수']
    ratios['비율'] = (ratios['인구수'] / region_data['2024년11월_계_총인구수'].values[0]) * 100
    max_age = ratios['비율'].idxmax()
    min_age = ratios['비율'].idxmin()
    return max_age, ratios['비율'].max(), min_age, ratios['비율'].min()

# 메인 스트림릿 앱
def main():
    st.title("지역별 인구 구조 분석")
    st.write("지역의 연령별 인구 구조를 시각화하고 최고/최저 비율을 찾습니다.")

    # 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일을 업로드해주세요.", type=['csv'])
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        # 지역 선택
        selected_region = st.selectbox("분석할 지역을 선택해주세요:", df['행정구역'].unique())

        # 선택한 지역의 연령별 인구 구조 시각화
        st.subheader(f"{selected_region}의 연령별 인구 구조")
        region_data = df[df['행정구역'] == selected_region]
        age_data = region_data.iloc[:, 4:].T
        age_data.columns = ['인구수']
        age_data.index = age_data.index.str.replace('2024년11월_계_', '').str.replace('세', '')
        age_data = age_data.reset_index().rename(columns={'index': '연령대'})

        # Plotly 그래프 생성
        fig = px.bar(age_data, x='연령대', y='인구수', title=f"{selected_region} 연령별 인구수")
        st.plotly_chart(fig)

        # 최고/최저 비율 계산
        max_age, max_value, min_age, min_value = find_max_min_ratio(df, selected_region)
        st.subheader("연령대별 최고/최저 비율")
        st.write(f"**최고 비율 연령대**: {max_age} ({max_value:.2f}%)")
        st.write(f"**최저 비율 연령대**: {min_age} ({min_value:.2f}%)")

if __name__ == "__main__":
    main()


streamlit run your_app_name.py
