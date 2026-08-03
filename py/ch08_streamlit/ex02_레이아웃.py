import streamlit as st

st.set_page_config(
    page_title="학생성적관리",
    page_icon="％",
    layout="wide"
)

st.title('페이지 설정이 완료된 애플리케이션')
st.write('이제 더 넓은 화면에서 볼 수 있습니다!')

# 레이아웃 컴포넌트

st.title("학생 정보관리 시스템")
# [DeltaGenerator]
# 4개의 열로 나누기
col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.metric("전체 학생 수", "245")

with col2:
    st.metric("평균 점수", "24582.5")

with col3:
    st.metric("출석률", "24582.5")

with col4:
    st.metric("과제 제출률", "87.7%")


# 컨테이너로 묶기
with st.container():
    st.subheader('이번 달 도서관 현황')
    st.write('이영역 에서는 도서관의 주요 통계가 표시됩니다.')
    st.metric("대출 도서 수 : ","1,245권")
    st.metric("신규회원","+23명")

# 확장 가능한 세션
with st.expander("상세 통계 정보"):
    st.write("여기에는 자세한 분석 결과가 들어갑니다.")
    st.write("평소에는 숨겨져 있다가 필요할 때만 펼쳐볼 수 있습니다.")


# 지표 카드 만들기

st.title('카페 매출 대시보드')

# 기본 지표
st.metric("오늘 매출","450,000원")

# 변화량과 함께 표시
st.metric(
    label="일일 방문객",
    value="127명",
    delta="+23명"
)

# 음수 변화량(빨간색으로 표시)
st.metric(
    label="재고 수량",
    value="85개",
    delta="-15개"
)


# 상태 메세지 표시하기

# 정보메세지
st.info('시스테 점검이 예정되어 있습니다.')

st.success('데이터 백업이 완료되었습니다.')

st.warning('일부 기능이 제한될 수 있습니다.')

st.error('서버 연결에 싶패했습니다.')

# 로딩 표시하기

import time

with st.spinner("학생데이티를 처리하는중..."):
    time.sleep(3)

st.success("처리완료!")

# 빈공간 관리하기

placeholder = st.empty()

# 나중에 내용 채우기

time.sleep(2)
placeholder.text('검색 결과가 나타났습니다!')

# 내용 교체하기
time.sleep(2)
placeholder.success('검색이 완료되었습니다.')