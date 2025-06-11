import streamlit as st
import pandas as pd
from datetime import datetime
import os







#--------------------전체 레이아웃(메인: 넓게, 사이드바: 넓게게)
st.set_page_config(
	layout="wide",
	initial_sidebar_state="expanded"
)

#--------------------해당 페이지 타이틀
st.title("가게부 대시보드")

st.markdown("가게부대시보드다!!!")


#-------------------- variables
base_dir = os.path.dirname(__file__) #playground/pages
file_path = os.path.join(base_dir, "..", "testData.xlsx") #playground/testData.xlsx
df = pd.read_excel(file_path) #원본 데이터

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



#-----메인페이지
st.write(
    f"선택된 날짜: {selected_start_date} ~ {selected_end_date}",
		df
)


