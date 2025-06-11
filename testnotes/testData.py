#%%
import pandas as pd
from datetime import datetime
import os


# %%
base_dir = os.path.dirname(__file__) #playground/pages
file_path = os.path.join(base_dir, "..", "testData.xlsx") #playground/testData.xlsx
df = pd.read_excel(file_path) #원본 데이터
df.head()


# %%
df['지출일'] = df['지출일'].astype(str).str.split(" ").str[0]
df.head()
