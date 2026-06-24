#제어문
#조건문
'''
탭키와 스페이스바를 섞어쓰면 안된다. 들여쓰기는 4칸를 원칙으로 한다.
PEM8 규칙이다. 스페이스바로 4칸하는게 정확하다. 
텝키는 세팅에 따라서 3칸 등 칸수가 다를기 때문이다.
if 조건식:   (반드시 :를 써야 한다.)
    수행문1
    수행문2
수행문 

if 조건식:
    수행문1
else:
    수행문2
조건식은 결과가  True아니면 Fulse여야 한다.
비교,논리(and,or,not) 연산의 결과
'''

today_temp = -30
if today_temp > 0:
    print("아이스 아메리카노")
else:
    print("라떼")

'''
if 조건식1:
    수행문1
elif 조건식2:
    수행문2

else:
    수행문3
'''

today_temp = 30
if today_temp > 0:
    print('아아')
elif today_temp == 0:
    print('라데')
else:
    print('핫아')

#중첩 if
weather = '비'
today_temp = 30
if weather == '맑음' :
    pass
else:
    print("먹지마!")

#pass 대신 if  구문을 추가
weather = '비'
today_temp = 30
if weather == '맑음' :
    if today_temp > 0:
        print('아아')
    elif today_temp == 0:
        print('라데')
    else:
        print('핫아')
else:
    print("먹지마!")

#복합조건
# 엄마안
math_score = 80
eng_score = 100

if math_score > 90 and eng_score > 90:
    print("용돈인상")
elif math_score <= 90 and eng_score <= 90:
    print('용돈삭감')
else:
    print('동결')

#아이안
math_score = 80
eng_score = 100

if math_score > 90 or eng_score > 90:
    print("용돈인상")
elif math_score <= 90 or eng_score <= 90:
    print('용돈삭감')
else:
    print('동결')