# 라이브러리 설치 및 데이터 로드
import yfinance as yf
import pandas as df

df = yf.download("NVDA", period="1y", interval="1d", multi_level_index=False)
print(df.head())



'''
1. *.py 실행 : F5 --> 터미널 실행(pycham에서는 기본값,VSC에서 아닐수 있다.
2. *.py : 실행할 코드 영역을 블록 설정 후 shift+ enter --> 인터프리터 실행
3. *.ipynb : shift+enter
'''

# Q1. 데이터 프레임(df)의 기본정보를 확인 (shape,info,describe)
print('======shape:======')
df.shape
print('\n=======info=======')
df.info()
print('\n=======describe=======')
df.describe()
#Q2
print('컬럼명:', df.columns.tolist()) 
#Q3 데이터 미리 보기
print('첫 5개 행')
print(df.head())
print('마지막 5개 행')
print(df.tail())
#Q4
print(f"종가 최대값: {df['Close'].max():,.0f}")
print(f"종가 최소값: {df['Close'].min():,.0f}")
print(f"종가 평균값: {df['Close'].mean():,.0f}")

#Q5
print(f"거래량 평균: {df['Volume'].mean():,.0f}")
print(f"거래량 중앙값: {df['Volume'].median():,.0f}")
print(f"거래량 표준편차: {df['Volume'].std():,.0f}")

#Q6
high_low_diff = df['High'] - df['Low']
print(f"고가 - 저가 차이 평균 : {high_low_diff.mean():,.0f}")
print(f"고가 - 저가 차이 평균 : {df['High'].mean():,.2f}")
print(f"고가 - 저가 차이 평균 : {df['Low'].mean():,.2f}")

#Q7
selected_df = df[['Close','Volume']].copy()
print(selected_df.head())

#Q8
recent_10 = df.tail(10)
print(recent_10)
#Q9
threshold = df['Close'].quantile(0.90)
high_price = df[df['Close'] >= threshold]
print(f"종가 {threshold:.2f} 이상인 날: {len(high_price)}일")
#Q10
avg_volume = df['Volume'].mean()
high_volume_days = df[df['Volume'] > avg_volume]
print(f"평균 거래량 {avg_volume:.2f}보다 많았던 날: {len(high_price)}일")
#Q11
volume_sorted = df.sort_values('Volume',ascending=False)
print(volume_sorted['Volume'].head())
#Q12
df['Daily_Change'] = df['Close'] - df['Open']
print(df[['Open','Close','Daily_Change']].head())
#Q13
df['Change_Rate'] = ((df['Close']-df['Open']) / df['Open']*100).round(2)
print(df[['Open','Close','Change_Rate']].head()) 
