import os
import pandas as pd





def load_data():
    '''
    데이터 불러오기 & 날짜 전처리리
    '''		
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "testData.xlsx")
    df = pd.read_excel(file_path)

    # 지출일 전처리
    df["지출일_날짜"] = df["지출일"].astype(str).str.split(" ").str[0]
    df["지출일_날짜"] = pd.to_datetime(df["지출일_날짜"], format="%Y.%m.%d").dt.date
    return df


def date_filter(df, start_date, end_date):
    '''
    선택된 날짜로 데이터 필터링
    '''
    cond1 = df['지출일_날짜'] >= start_date
    cond2 = df['지출일_날짜'] < end_date
    return df[
        (df["지출일_날짜"] >= start_date) &
        (df["지출일_날짜"] <= end_date)
				]
