# 건강검진 시각화 실습
# 건강검진 데이터 시각화
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 한글을 지원하는 그꼴 변경
plt.rcParams['font.family'] = 'NanumGothic'

df = pd.read_csv("국민건강보험공단_건강검진정보_2023.csv",encoding='euc-kr')

df.head()
df.describe()
df.info()

#1. 불필욯한 컬럼 제거
df.drop(
    ['기준년도','가입자일련번호'
     '결손치 유무','치아마모증유무',
     '제3대구치(사랑니) 이상'], inplace=True, axis=1
)

df.rename(
    columns={'연령대코드(5세단위)':'연령코드',
             '신장(5cm단위)':'신장',
             '체중(5kg단위)':'체중',
             '식전혈당(공복혈당)':'혈당'
        }, 
        inplace=True
)



df.info()

#결측치(NaN) 제거
df = df.dropna()

df.info()

# 전체 데이타 분포 시각화
fig, axs=plt.subplots(5,5)
fig.set_size_inches(20,24)

for i in range(0,5):
    for j in range(5):
        attr = i * 5 + j + 1
        if df[df.columns[attr]].nunique() < 30:
            sns.countplot(x=df.columns[attr], data=df, ax=axs[i][j])
        else:
            sns.histplot(x=df.columns[attr], data=df, kde=True, ax=axs[i][j])

df
df.columns
attr
df.columns[attr]
df['음주여부'].nunique()

# 상관관계 분석
# 혈압 데이타 상관관계

sns.scatterplot(x=df['수축기혈압'],y=df['이완기혈압'],hue=df['흡연상태'])

# 신장가 체중 상관관계
sns.scatterplot(x=df['신장'],y=df['체중'],hue=df['성별코드'])


# 혈당과 총 콜레스테롤 상관관계
sns.scatterplot(x=df['혈당'],y=df['총콜레스테롤'],hue=df['성별코드'])

# 나이에 따른 총 콜레스테롤 추이

sns.lineplot(x=df['연령코드'],y=df['총콜레스테롤'])


# 연령에 따른 혈색소 수치 분포
fig = plt.figure(figsize=(10,5))
sns.boxplot(x=df['연령코드'], y=df['혈색소'])

#연령과 성별에 따른 혈당 분석
fig = plt.figure(figsize=(12,5))
sns.barplot(x=df['연령코드'], y=df['혈당'],hue=df['성별코드'] )

# 나이에 따른  허리둘레 분포

fig = plt.figure(figsize=(12,5))
sns.violinplot(x=df['연령코드'], y=df['허리둘레'],hue=df['성별코드'] )
