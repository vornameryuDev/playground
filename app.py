import streamlit as st


#-----웹페이지 마스터 제목
st.set_page_config(
	page_title="민수의 놀이터",
	page_icon="😎"
)

#-----타이틀
st.markdown(
	'''
	# 민수의 놀이터에 온걸 환영해!
	아래에서 여러가지를 확인해보쟈><

	- [accountBook](/가게부확인)
	- [realEstate](/청약확인)
'''
)


# ----- 사이드바 목록
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/vornameryuDev" target="_blank">GitHub 링크</a>
    </div>
    """,
    unsafe_allow_html=True
)

