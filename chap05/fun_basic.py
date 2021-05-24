def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)
            # 단순한 줄바꿈
            print()
# 함수 호출
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print()

def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)
# 함수 호출
print_n_times("안녕하세요")
print()

# print("# 기본 매개변수가 가변 매개변수보다 앞에 올때")
# def print_n_times(n=2, *values):
#     # n번 반복합니다.
#     for i in range(n):
#         # values 는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#             # 단순한 줄바꿈
#             print()
# # 함수 호출
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")
# print()

print("# 가변 매개변수가 기본 매개변수보다 앞에 올때")
def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)
            # 단순한 줄바꿈
            print()
# 함수 호출
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3)
print()

print("# 키워드 매개 변수")
def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)
            # 단순한 줄바꿈
            print()
# 함수 호출
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
print()

print("# 기본 매개변수 중에서 필요한 값만 입력")
def test(a, b=10, c=100):
    print(a + b + c)

# 1) 기본 형태
test(10, 20, 30)
# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)
# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)
# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)

