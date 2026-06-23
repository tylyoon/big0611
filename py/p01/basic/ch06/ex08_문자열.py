#문자열 분리 - split()
text = "나는 자랑스러운 태극기 앞에 자유롭고 정의로운 대한민국의 무궁한 영광을 위하여 충성을 다할 것을 굳게 다짐합니다."


print(text.split())

text = "+82-10-1234-5678"
print(text.split('-'))
# -1이 default 이며 제한이 없다. 2는 최대 분라 숫자.,최대구분갯수
# split(sep='-',maxsplit = 2)
# 2의 의미는 2개만 구분자 사용하여 구분하고, 나머지는 하나로 처리한다.
print(text.split('-',2))

#공백 제거 함수 9좌우공백만 제거
#strip : 좌우 모두
#lstrip : 왼쪽만
#rstrip : 오른쪽만

text = "        토실토실 아기 돼지        "
print(text.strip())
text = "        토실토실 아기 돼지        "
print(text.rstrip())
print(text.lstrip())

text = "\n\n\n\n토실토실2 아기 돼지\n\n\n\n"
print(text.strip('\n'))
print(text)
print(text.strip())

#문자가 중간에 있으면 지우지 못한다.
text = "XXaaaaa토실토실 아기 돼지aaaaa"

print(text.strip("a"))

text = "ababab토실토실 아기 돼지ababab"
print(text.strip("ab"))

text = "aaabbbccccc토실토실 아기 돼지aaabbbccccc"
print(text.strip("abc"))

#strip("문자") 문자를 모두 지움,text 값은 유지됨

# 문자열 연결 - join()
# 문자열1.join(문자열2)
text1 = "->"
text2 = ["인천", "도쿄", "뉴욕", "파리"]
print(text1.join(text2))

#문자열 검색
#문자열1.find('문자열2',스타트번호) 문자열1에서 문자열2를 찾는다.
# 반환값은 지가 위치한 첫번째 인덱스 번호를 반환한다. 
text = "송아지 송아지 얼룩 송아지 지"
print(text.find("지"))
print(text.find("얼룩"))
print(text.find("지",3))

#문자열 갯수 세기
#문자열1.count('문자열2')

print(text.count('송아지'))

#시작과/끝 문자열 확인
#있으면 True,없으면 False
#startswith(접두사)
#endswith(접미사)

animals = ['사자','송아지','돼지','사슴']
for i in animals:
    print(i.startswith('사'))

for i in animals:
    print(i.endswith('지'))

#문자열 치환
#문자열1에서 문자열2를 찾아 문자열3으로 변경
#문자열1.replace('문자열2','문자열3')

text = '강아지'
print(text.replace('강', '송'))

#대소문자 변환
#lower()
#upper()

text = 'Coffee'
print(text.lower())
low = text.upper()
print(low)
print(low.upper())

# 사용자 명단 처리 시스템
'''
사용자로부터 여러 명의 이름을 입력받아 데이터를 정제하고 분석하는 프로그램을 작성하시오.
(요구사항)
1. 입력 데이터: " 오리, 이기자, 배철수다 " (앞뒤 공백 포함)
2. 데이터 정제: 앞뒤 공백 제거
3. 이름 분리: 쉼표와 공백(",")을 기준으로 이름들을 리스트로 분리
4. 결과 출력: 다음 형식으로 출력

(예상 출력)
=== 사용자 명단 처리 결과 ===
원본 데이터: ' 오리, 이기자, 배철수다 '
정제된 데이터: '오리,이기자,배철수디'
분리된 이름 목록: ['오리', '이기자', '배철수다']
1번째 사용자: 오리 (길이: 3자)
2번째 사용자: 이기자 (길이: 3자)
3번째 사용자: 배철수다 (길이: 3자)
'''

#1. 입력 데이터: " 오리, 이기자, 배철수다 " (앞뒤 공백 포함)
user_input = " 오리, 이기자, 배철수다 "
#2. 데이터 정제: 앞뒤 공백 제거
clean_input = user_input.strip()
#3. 이름 분리: 쉼표와 공백(",")을 기준으로 이름들을 리스트로 분리
names_list = clean_input.split(',')
#4. 결과 출력: 다음 형식으로 출력

print('=== 사용자 명단 처리 결과 ===')
print(f'원본 데이터:{user_input}')
print(f'정제된 데이터:{clean_input}')
print(f'분리된 이름 목록:{names_list}')



#enumerate(iterable객체, 시작인덱스)
#len('문자역'):문자열의 길이
for i, name in enumerate(names_list,1):
    print(f'{i}번째 사용자: {name} (길이: {len(name)})')

