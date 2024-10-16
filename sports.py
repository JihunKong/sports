import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 제목
st.title('Daily Exercise Tracker')

# 사용자가 기록할 수 있는 폼
st.header('Record your exercise')

# 입력받을 운동 정보
exercise = st.text_input('Exercise')
duration = st.number_input('Duration (minutes)', min_value=0)
date = st.date_input('Date', value=datetime.now())

# 기록된 데이터를 저장할 데이터프레임 생성
if 'exercise_data' not in st.session_state:
    st.session_state.exercise_data = pd.DataFrame(columns=['Date', 'Exercise', 'Duration'])

# 기록 버튼
if st.button('Record'):
    new_data = pd.DataFrame({'Date': [date], 'Exercise': [exercise], 'Duration': [duration]})
    st.session_state.exercise_data = pd.concat([st.session_state.exercise_data, new_data], ignore_index=True)
    st.success('Recorded successfully!')

# 현재까지의 운동 기록 표시
st.header('Your exercise records')
st.dataframe(st.session_state.exercise_data)
