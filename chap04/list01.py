# 리스트 선언
list_a = [1,2,3]
list_b = [4,5,6]

#출력
print("# 리스트")
print("list_a =", list_a)
print()

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

# 함수
print("# 리스트 길이 구하기")
print("len(list_a) =", len(list_a))
print()

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가
print("# 리스트 중간에 요소 추가")
list_a.insert(0, 10)
print(list_a)
print()

# 리스트의 요소 하나 제거하기
list_a = [0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거")

# 제거 방법[1] - del
del list_a[1]
print("del list_a[1] :", list_a)

# 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2) :", list_a)
print()

# for 반복문 : 리스트와 함께 사용
print("# 리스트에 반복문을 적용")
# 리스트를 선언
array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용
for element in array:   # for 반복자 in 반복할 수 있는 것: 코드
    #출력
    print(element)


