# while 반복문: for 반복문처럼 사용

# 반복 변수를 기반으로 반복
print("# 반복 변수를 기반으로 반복")
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1
print()

# 상태를 기반으로 반복
# 해당하는 값 모두 제거
print("# 해당하는 값 모두 제거")

# 변수 선언
list_test = [1, 2, 1, 2]
value = 2

# list_test 내부에 value 가 있다면 반복
while value in list_test:
    list_test.remove(value)

# 리스트 내부에 있는 2가 제거될 때 까지 반복, 2가 모두 제거된 결과가 출력
print(list_test)

