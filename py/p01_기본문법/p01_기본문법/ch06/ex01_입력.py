# with는 함수가 아니다.
# 시스템 입력
# input()
# 샤용자로 부터 이름을 입력받고, 이름과 함께
# 인사말을 출력
# 사용자로 부터 이름을 입력 받느다.

name = input("이름을 입력하세요:")
#print(name + "님,안녕하세요") 
print(f'{name}님,안녕하세요')


#외부에서 입력받은 input 값은 문자이다.

height = int(input("키을 입력하세요 : "))
# weight = (int(height) - 100) * 0.9
weight = (height - 100) * 0.9
print(f'권장 체중은 {weight}kg 입니다.')
