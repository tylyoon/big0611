
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import numpy as np

from datetime import datetime, timedelta


# 학생성적 데이타 만들기

data = {
    '이름' : ['김철수','이영희','박민수','최지연'],
    '수학' : [85,92,78,96],
    '영어' : [88,85,90,93],
    '과학' : [90, 88, 85, 89]
}

df = pd.DataFrame(data)

st.title('학생 성적 데이터 표시하기')
st.dataframe(df)

# 표 스타일링 하기

sales_data = {
    '상품명': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    '가격': [1200000, 25000, 80000, 350000, 150000],
    '판매량': [15, 120, 85, 30, 45],
    '평점': [4.5, 4.2, 4.7, 4.1, 4.6]
}

df = pd.DataFrame(sales_data)

# 평점에 따라 색깔 적용
def color_rating(val):
    if val >= 4.5:
        color = 'green'
    elif val >= 4.0:
        color = 'orange'
    else:
        color = 'red'
    return f'color: {color}'

# 스타일 적용해서 표시
# style.format()으로 숫자 형식을 지정하고, map()으로 색깔 적용
# Pandas 2.1.0 버전부터 applymap() -> map()으로 변경
styled_df = df.style.format({
    '가격': '{:,}원',
    '판매량': '{:,}개',
    '평점': '{:.1f}점'
}).map(color_rating, subset=['평점'])

st.dataframe(styled_df)

# 3. 정적 테이블 만들기
# 날씨 정보 표시용 정적 테이블
weather_data = {
    '항목': ['최고 기온', '최저 기온', '습도', '강수 확률'],
    '값': ['28°C', '18°C', '65%', '30%']
}

weather_df = pd.DataFrame(weather_data)
st.table(weather_df)

# 기본 차트 컴포넌트
# 1. 선 그래프로 추세 보기
'''
- 시간에 따른 변화를 가장 직관적으로 보여주는 방법은 선 그래프이다.
- st.line_chart)는 시간에 따른 변화를 보여주는 선 그래프를 만든다.
- 웹 사이트 트래픽처럼 시간 순서가 중요한 데이터에 적합하다.
'''
# 웹사이트 방문자 수 데이터 만들기


dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
visitors = np.random.randint(100, 500, 30)

visitor_df = pd.DataFrame({
    'Date': dates,
    'Visitors': visitors
})

st.title('기본 차트 예시')
st.subheader('웹사이트 일일 방문자 수')
# st.line_chart(data=visitor_df, x='Date', y='Visitors')
# 사용버젼 확인 pip show streamlit
st.line_chart(visitor_df.set_index('Date')['Visitors'])

# 2. 막대 그래프로 비교하기
'''
- 여러 카테고리의 값을 비교할 때는 막대 그래프가 좋다.
- 막대의 높이로 값의 크기를 직관적으로 비교할 수 있다.
- 도시별 인구수처럼 카테고리 간 비교에 효과적이다.
'''
# 도시별 인구 비교
population_data = {
    '서울': 9720000,
    '부산': 3390000,
    '인천': 2950000,
    '대구': 2410000,
    '대전': 1490000
}

population_df = pd.DataFrame(list(population_data.items()), columns=['도시', '인구수'])

st.subheader('주요 도시 인구 비교')
st.bar_chart(population_df.set_index('도시')['인구수'])
print(list(population_data.keys()))
print(list(population_data.values()))
print(list(population_data.items()))

# 3. 영역 차트로 누적 보기
'''
- 시간에 따른 여러 요소의 변화를 함께 보여줄 때는 영역 차트를 사용한다.
'''
# 월별 매출 구성 비교
monthly_data = pd.DataFrame({
    'Date': dates,
    '온라인_매출': np.random.randint(50, 150, 30),
    '오프라인_매출': np.random.randint(80, 200, 30),
    '모바일_매출': np.random.randint(30, 100, 30)
})

st.subheader('채널별 매출 구성 변화')
st.area_chart(monthly_data.set_index('Date'))




# plotly 차트 통합
# 1. 인터랙티브 차트의 장점
st.title('Plotly 차트 통합')

# 제품 판매량 데이터 생성
dates = [datetime.now() - timedelta(days=x) for x in range(100, 0, -1)]
np.random.seed(42)
sales = np.random.randint(50, 200, 100)

# Plotly 선 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dates,
    y=sales,
    mode='lines',
    name='일일 판매량',
    line=dict(color='blue', width=2)
))

fig.update_layout(
    title='인터랙티브 판매량 차트',
    xaxis_title='날짜',
    yaxis_title='판매량 (개)',
    height=400
)

# use_container_width=True를 사용하면 화면 크기에 맞춰서 차트가 조정된다.
st.plotly_chart(fig, use_container_width=True)


# 2. 산점도 차트 만들기
# 산점도는 두 변수 간의 상관관계를 시각적으로 파악할 때 유용하다.
# 광고비와 매출의 관계
np.random.seed(42)
ad_spend = np.random.randint(10, 100, 50)
revenue = ad_spend * 2.5 + np.random.normal(0, 20, 50)

scatter_fig = go.Figure()
scatter_fig.add_trace(go.Scatter(
    x=ad_spend,
    y=revenue,
    mode='markers',
    name='데이터 포인트',
    marker=dict(
        size=8,
        color='lightblue',
        line=dict(width=1, color='navy')
    )
))

scatter_fig.update_layout(
    title='광고비 vs 매출 관계',
    xaxis_title='광고비 (만원)',
    yaxis_title='매출 (만원)',
    height=400
)

st.subheader('산점도 차트')
st.plotly_chart(scatter_fig, use_container_width=True)

# 3. 파이 차트로 비율 보기
# 전체에서 각 부분이 차지하는 비율을 보여줄 때는 파이 차트를 사용한다.
# 파이 차트는 전체 100%에서 각 항목이 차지하는 비율을 직관적으로 보여준다.
# 설문조사 결과

survey_data = {
    '매우 만족': 25,
    '만족': 40,
    '보통': 20,
    '불만족': 10,
    '매우 불만족': 5
}

pie_fig = go.Figure(data=go.Pie(
    labels=list(survey_data.keys()),
    values=list(survey_data.values()),
    hole=0.3
))

pie_fig.update_layout(
    title='고객 만족도 설문 결과',
    height=400
)

st.subheader('만족도 분포')
st.plotly_chart(pie_fig, use_container_width=True)



# 4. 히스토그램으로 분포 보기
# 히스토그램은 데이터의 분포를 시각적으로 보여준다.
# 히스토그램은 데이터가 어떤 구간에 얼마나 많이 분포하는지 보여준다.
# 학생들의 키 분포


np.random.seed(42)
heights = np.random.normal(170, 10, 200)

hist_fig = go.Figure()
hist_fig.add_trace(go.Histogram(
    x=heights,
    nbinsx=20,
    name='키 분포',
    marker_color='lightblue'
))

hist_fig.update_layout(
    title='학생 키 분포',
    xaxis_title='키 (cm)',
    yaxis_title='학생 수',
    height=400
)

st.subheader('키 분포 히스토그램')
st.plotly_chart(hist_fig, use_container_width=True)





