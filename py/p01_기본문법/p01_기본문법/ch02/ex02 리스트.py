# 리스트 [  ]
# 튜플 (  )
# 세트 {  }
# 딕셔너리 { key : item, ..}
# 여러단어 다중 선택 : ctrl + d
# 생성

# CRUD (Create,Read,Update,Delete)
# 리스트 아이템 선택
# 인텍싱
fruit_list = ['apple','banana','orange']
print(fruit_list[0])
print(fruit_list[-1])
#스라이싱


#아이템 수정 (Update)
fruit_list[1] = 'kiwi'
print(fruit_list[1])

#추가
#insert()
#append()
#메서드 객체가 붙어있으면 메서드 객체.insert()
#함수() 객체가 없으면 함수 print()

# list객체.insert(인덱스,아이텤)
fruit_list.insert(2,'망고')
print(fruit_list)
# list객체.append(아이템) : 끝에 추가
fruit_list.append('수박')
print(fruit_list)
#확장 list1.extend(list2)
vegetable_list = ['당근','토마토','양파']
fruit_list.extend(vegetable_list)
print(fruit_list)

# + 연산
list1 = [1,2,3]
list2 = ['가','나','다']
list1 = list1+list2
print(list1)

#삭제
#리스트.remove(아이템)
fruit_list.remove('토마토')
print(fruit_list)

# del 리스트[인텍스]
del fruit_list[1:3]
print(fruit_list)
#del 리스트
#del vegetable_list
#print(vegetable_list)
#clear
#fruit_list.clear()
print(fruit_list)

#정렬 (sort) 리스트.sort()
'''
- 오름차순 : 1,2,3,4  가,나,다 a,b,c
- 내림차순 : 4,3,2,1  다,나,가 c,b,a

'''

fruit_list.sort()
print(fruit_list)

fruit_list.sort(reverse=True)
print(fruit_list)

fruit_list.clear()
print(fruit_list)

