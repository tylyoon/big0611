#예외(exception)
#예외처리
"""
try:
    예외가 발생할 수 있는 코트
except 예외타입 as e:
    print(e)
except 예외타입 as e:
    print(e)
except:
    예외처리
finally:
    항상 마지막으로 실행되는 코드
"""

# 나이 입력 및 검증 시스템
def get_valid_age():
    while True:
        try:
            age = int(input('나이를 입력하세요:'))
            
    # ValueError: invalid literal for int() with base 10: '다섯살'
    # TypeError: '<' not supported between instances of 'str' and 'int'
            if age < 0 :
                print('나이는 0 이상이어야 합니다.')
                continue

            elif age > 150:
                print('유효하지 않은 나이입니다')
                continue
            else:
                return age
        except ValueError as e:
            print(f'숫자만 입력해주세요:{e}')
        except KeyboardInterrupt:
            print('\n프로그램을 종료합니다.')
    

#하수 호출
try :
    user_age = get_valid_age()
    if user_age:
        print(f'입력하신 나이는 {user_age}세 입니다.')
except :
    print('예상하지 못한 오류가 발생했습니다.')

