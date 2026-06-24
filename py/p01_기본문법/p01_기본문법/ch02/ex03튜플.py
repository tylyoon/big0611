#투플(tuple)
fruit_tuple = ('사과','바나나','오렌지')
print(fruit_tuple)

fruit_tuple = ('사과','바나나','오렌지','사과','바나나')
print(fruit_tuple)

# 선택
# 인텍싱
fruit_tuple[1]
print(fruit_tuple[1])

#수정(Update) tuple은 수정을 할 수 없다.
#fruit_tuple[1] = '키위' Type error

#추가 : insert,append도 tuple은 append 메서드(attribute)가 없다.
#fruit_tuple.append('수박')
#삭제도 안된다. 'tuple' object has no attribute 'remove'
#fruit_tuple.remove('바나나')
# 타입 변환
# 기본 : int(),float(),str(),bool()
# 컨테이너 : list(),tupe(),set(,dict())
# del은 적용됨
print(fruit_tuple)
fruit_list = list(fruit_tuple)
fruit_list.append('수박')
fruit_list.remove('사과')
fruit_list[1] = '키위'
print(fruit_list)
fruit_tuple = tuple(fruit_tuple)
print(fruit_tuple)
#fruit_tuple.clear()
#print(fruit_tuple)
