# 함수 정의
def return_test():
    print("A 위치입니다.")
    return  # 리턴
    print("B 위치입니다.")

return_test()
print()

def return_test():
    return  100

value = return_test()
print(value)
print()

def return_test():
    return

value = return_test()
print(value)
print()

print("# 범위 내부의 정수를 모두 더하는 함수")
# 함수 선언
def sum_all(start, end):
    # 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        output += i
    return output   # 리턴
# 함수 호출
print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))
print()

print("기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수")
# 함수 선언
def sum_all(start=0, end=100, step=1):
    # 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        output += i
    return output   # 리턴
# 함수 호출
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
print()