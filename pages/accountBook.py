import streamlit as st
import pandas as pd
from datetime import datetime
import os

from funcs.accountBook import date_filter, load_data







#--------------------전체 레이아웃(메인: 넓게, 사이드바: 넓게게)
st.set_page_config(
	layout="wide",
	initial_sidebar_state="expanded"
)

#--------------------해당 페이지 타이틀
st.title("가게부 대시보드")

st.markdown("가게부대시보드다!!!")


#-------------------- variables
df = load_data() #데이터불러오기

today = datetime.today().date() #오늘날짜 기준 설정
min_year = 2023
max_year = 2025




#-----사이드바
# sidebar 내에 구성
with st.sidebar:
    st.header("📅 기간 선택")
    
		#시작날짜
    selected_start_date = st.date_input(
				"시작날짜를 선택하세요",
				value=today,
				min_value=datetime(min_year,1,1).date(),
				max_value=datetime(max_year,12,31).date()
		)    
    #종료날짜
    selected_end_date = st.date_input(
				"종료날짜를 선택하세요",
				value=today,
				min_value=datetime(min_year,1,1).date(),
				max_value=datetime(max_year,12,31).date()
		)
    #조회버튼
    col1, col2 = st.columns([3, 1])
    with col2: 
					search_btn = st.button("조회")



#-----메인페이지
if search_btn:
    st.write(
    		f"선택된 날짜: {selected_start_date} ~ {selected_end_date}",
        filterd_df = date_filter(df, selected_start_date, selected_end_date)       
		)
else:
    st.write(f"날짜 기본값입니다. 오늘(today)기준 30일 전의 데이터만 가져올겁니다다.")
