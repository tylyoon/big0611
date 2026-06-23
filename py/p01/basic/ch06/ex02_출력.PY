
print("사과","복숭아","망고")
# 구분자 ,
print("사과","복숭아","망고", sep = ',')

#줄바꿈
# 기본값: end ='\n'
print('이것은 문장입니다.', end = '\n')
print('문장입니다.', end = '')
#주바꿈 안됨
print('이것은 문장입니다.', end = '')
print('문장입니다.', end = '')

#문자열 연결 : +
#나이: 20살
age = 20
# age가 숫자면 str()로 변환 시켜야 합니다.
print('나이 : '+ str(age) + '살')

#줄바꿈 : \n
print("산토끼 토끼야 \n 어디를 가느냐 \n 깡총깡총 뛰어서 \n 어디를 가느냐")

# 포매스트링
'''
print('메시지{} {}'.format(값1,값2,..))
print('메시지 : {0} {1}'.format(값1,값2,..))

'''

food = '치킨'
text = '나는 {}을 먹고 싶다'
print(text.format(food))
print('나는 {}을 먹고 싶다'.format(food))

food1 = '피자'
food2 = '치킨'
text = '나는 {} {} 을 먹고 싶다'
print('나는 {} {}을 먹고 싶다'.format(food1,food2))

text = '나는 {0} {1} 을 먹고 싶다'
print(text.format(food1,food2))

text = '나는 {1} {0} 을 먹고 싶다'
print(text.format(food1,food2))

print('나는 {} {}을 먹고싶다. 우리집엔 {}이 배달되지 않아 슬프다.'.format(food1,food2,food2))

# 인텍스 대신 벼수 이름으로
text = '{name}님, 반갑습니다. 적립금은 {money}원 입니다.'
print(text.format(name='홍길동',money = 500))

# 문자열에 %s를 작성하여, 치환할 문자를 지정한다.
# %s 문자, %f 실수, %d 정수
food = '치킨'
print('나는 %s을 먹고싶다.'% food)
print('{:.2f}% 확신합니다.'.format(95.1254567))

# 천단위마다 ,
print('한 달 휴대폰 요금은 {:,}원 입니다.'.format(100000))



# F string 방식
name = "철수"
age = 25
print("이름: %s, 나이: %d세" % (name, age))
print(f"이름: {name}, 나이: {age}세")

pi = 3.141592
print("원주율: %.2f" % pi)
print("원주율: {:.2f}".format(pi))
print(f"원주율: {pi:.2f}") 
