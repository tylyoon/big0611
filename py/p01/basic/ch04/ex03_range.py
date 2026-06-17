# range(start,stop,step)
# start : 0 (default)

for i in range(5):
    print(i,end=" ")

for i in range(2,7):
    print(i,end=" ")

for i in range(2,27,3):
    print(i,end=" ")

for i in range(27,3,-3):
    print(i,end=" ")
# print(range()) (안에 숫자있어야)
print(list(range(27,3,-3)))

# range(9) = range(0,9,1)
for num in range(1,10,1):
    print("3*{} = {}".format(num,(num)*3))

#하루에 5쪽, 20일 공부 일정

bookmark = 0
for day in range(20):
    print("[{}일차 공부계획]".format(day + 1))
    for page in range(5):
        print("{}쪽 공부".format(bookmark + page + 1))
    bookmark = bookmark + page +1

# 구구단
for dan in range(1,10,1):
    print('==={}단===='.format(dan),end=" ")
print() 
for num1 in range(1,10,1):
    for num2 in range(1,10,1):   
        print('{} * {} = {}'.format(num2,num1,num1*num2),end=" ")
    print()
 
#상품 재고 관리 시스템




