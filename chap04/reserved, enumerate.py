# reversed() 함수
# 리스트에서 요소 순서 뒤집기
# 리스트 선언
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) :", list_reversed)
print("list(reversed[1, 2, 3, 4, 5]):", list(list_reversed))
print()

# 반복문 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("_", i)
print()

# 확장 슬라이싱
print("# 확장 슬라이싱")
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[::-1])

print("안녕하세요")
print("안녕하세요"[::-1])
print()

# enumerate() 함수 - 리스트의 요소를 반복시 현재 인덱스가 몇 번째인지 확인할때 사용
# 변수 선언
example_list = ["요소A", "요소B", "요소C"]

# 그냥 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용해 출력
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수를 조합하여 사용
print("# 반복문과 조합하기")
# enumerate() 함수를 사용시 반복 변수를 아래 형태로 넣을 수 있음
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))