# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_time(func):
    for i in range(10):
        func()

# 조합 (매개변수로 함수를 전달)
call_10_time(print_hello)