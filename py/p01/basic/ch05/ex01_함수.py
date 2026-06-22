# 함수
'''
def 함수명():
    실행문
'''
def test():
    print("함수 연습")

#함수 호출
'''
함수명(인자1,인자,....)
실행문
return 값;
'''
test()

# 매개변수가 있는 함수
def coffee(temp):
    if temp > 0:
        print("아아")
    else:
        print("핫아")

coffee(20)

#재사용
#return 키워드

def coffee(temp):
    result = ''
    if temp > 0:
        result = '아아'
    else:
        result = '핫아'
    return result

c = coffee(30)
print('추천 커피는' + c + '입니다.')
#문자열.format
print('추천 커피는 {}입니다.'.format(c))
#f-string
print(f'추천 커피는 {c}입니다.')

c = coffee(-10)
print(f'추천 커피는 {c}입니다.')

#점수 업데이트 함수

def update_scores(scores):

    new_scores = []
    for score in scores:
        new = score + 5
        new_scores.append(new)

    return new_scores

scores = [80,90,70,65,85,95,90,80,75,80]
print(scores)
new = update_scores(scores)
print(new)

# 여러개의 매개변수
def get_char_count(lyric,char):
    count = 0
    for txt in lyric:
        if txt == char:
            count += 1
    return count

lyric = """산토끼 토끼야. 어디를 가느냐. 깡충깡충 뛰면서. 어디를 가느냐.
산고개 고개를. 나혼자 넘어서. 토실토실 알밤을. 주워 올 테야."""

rabbit = get_char_count(lyric,'토')
print(rabbit)

# 문자열.upper():대소문자
# 문자열.lower():소문자로

def change_word_case(word):
    upperCase = word.upper()
    lowerCase = word.lower()
    return upperCase, lowerCase

# a, b = 1, 2
# upper,lower = upperCase,lowerCase
upper, lower = change_word_case('I love Seoul.') 

print('대문자 {}이고,소문자는 {}이다.'.format(upper, lower))

# 사칙연산 계산기
def calculator(operator, num1,num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 !=0:
            return num1 / num2
    else:
        print('{}는 연산이 불가는합니다.')
        format((operator))
    return -1

print(calculator('+',200,300))
print(calculator('*',200,300))
print(calculator('-',200,300))
print(calculator('?',200,300))

#매개변수에 초기값 지정

def print_weight(height,man=True):
    weight = 0
    if man:
        weight = height - 100
    else :
        weight = (height - 100) * 0.9
    print('권장 체중은 {}kg 입다.'.format(weight))

print_weight(170)
print_weight(170,False)

#def print_weight(man=True,height):  syntext error 
# 갸변 인자
# *args를 사용하면 개수에 제한 없이 여러 이자를
# 튜플 현대로 받을 수 있다.

def sum(*args):
    print(type(args))
    print(args)
    result = 0
    for num in args:
        result += num
    return result



sum(1,2,3)

