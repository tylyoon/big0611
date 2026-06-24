
# ⭕ 이스케이프 시퀀스(\") 사용
# print("그는 "안녕"이라고 말했다.")
print("그는 \"안녕\"이라고 말했다.")
# 출력 결과: 그는 "안녕"이라고 말했다.

# 1. 줄바꿈(\n)과 탭(\t)
print("순위\t이름\n1등\t홍길동\n2등\t임꺽정")

# \t가 '탭'으로 오인되는 것을 막기 위해 두 번 적어줍니다.
print("C:\\Users\\test\\Documents")
# 출력 결과: C:\Users\test\Documents

# 문자열 앞에 r을 붙이면 내부의 \를 있는 그대로 문자 취급합니다.
path = r"C:\Users\test\Documents"
print(path)
# 출력 결과: C:\Users\test\Documents
# 리눅스,유닉스에서
path = "C:/Users/test/Documents"