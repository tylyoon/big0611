import streamlit as st
#st_autorefresh(interval=1000, key='datarefresh')
# st_autorefresh()
# streamlit run my_first_app.py

st.title('안녕하세요 Streamlit')
st.write(' 나의 첫 번째 Streamlit 애플리케이션입니다.')

# 제목과 헤더 만들기
st.title('이것은 가장 큰 제목입니다.') # 2.75rem = 44px
st.header('이것은 큰 헤더입니다.')  # 2.25rem = 36px
st.subheader('이것은 작은 헤더입니다.') # 1.75rem = 28px

# 일반 텍스트 표시하기
st.text('이것은 일반적인 텍스트를 작성할 수도 있습니다.') # 1rem = 16px

# 3. 마크다은으로 꾸미기
st.markdown('**이것은 굵은 글씨입니다.**')
st.markdown('*이것은 기울어진 글씨입니다.*')
st.markdown('**이것은 `인라인 코드` 입니다.**')

# 4. 만능 출력 함수
st.write('안녕하셍요.')
st.write(123)
st.write([1,2,3,4,5])

# 입력 커포넌트
#1. 선택 상자 만들기
# 좋아하는 과일 선텍
fruit = st.selectbox(
    '좋아하는 과일을 선택하세요.',
    ['사과', '바나나', '오렌지', '포도']
)
st.write(f'당신이 선택한 과일은 {fruit} 입니다.')

# 텍스트 입력 받기
name = st.text_input('이름을 입력하세요.')
age = st.number_input('나이를 입력하세요.', min_value=0,max_value=120)

if name and age:
    st.write(f'{name}님은 {age}살 입니다.')

# 슬라이더로 값 조정하기
temperature = st.slider('온도를 선택하세요',0, 40, 25)
st.write(f'선택한 온도는 {temperature}도 입니다.')

# 라디오 버튼과 체크박스
color = st.radio(
    '좋아하는 색깔을 선택하세요',
    ['빨강', '파랑', '초록']
)

agree = st.checkbox('이용약관에 동의합니다.')

if agree:
    st.write('동의해주셔서 감사합니다.')

# 여러개 선택하기
hobbies = st.multiselect(
    '취미를 선택하세요 (여러개 선택 가능)',
    ['독서','여화감상','운동','여행','음악감상']
)

# 날짜와 시간 입력
from datetime import datetime
today = st.date_input('날짜를 선택하세요')
current_time = st.time_input('시간을 선택하세요')
st.write(f'선택한 날짜: {today}')
st.write(f'선택한 날짜: {current_time}')

# 이미지 표시하기
#st.image('https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ba819fd9-0bb-401a-9136-9fe3fcd23111/Home_Page.png',caption='예시 이미지')
#st.image('my_image.jpg',caption='내 이미지')

st.image('https://picsum.photos/id/1000/300/200',caption='인터넷 이미지')

#오디오 파일 생성
#mp3(노래),ogg(ogv),
# st.audio('my_audid.mp3')
#비디오 파일 재생
# st.video('my_video.mp4')
# 유튜브 비디오 표시
# html에서는 <iframe src="경로/파일명"></iframe>사용한다.
st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', width=300)