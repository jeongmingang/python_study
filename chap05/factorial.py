print("# 반복문으로 팩토리얼 구하기")
# 함수 선언
def factorial(n):
    # 변수 선언 
    output = 1
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(1, n + 1):
        output *= i
    return output   # 리턴
# 함수 호출
print("1!:", factorial(1))
print("1!:", factorial(2))
print("1!:", factorial(3))
print("1!:", factorial(4))
print("1!:", factorial(5))
print()

print("# 재귀함수를 사용해 팩토리얼 구하기")
# 함수 선언
def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    # n이 0이 아니라면 n * (n-1)!을 리턴
    else:
        return n * factorial(n - 1)
# 함수를 호출합니다.
print("1!:", factorial(1))
print("1!:", factorial(2))
print("1!:", factorial(3))
print("1!:", factorial(4))
print("1!:", factorial(5))
print()

print("# 재귀 함수로 구현한 피보나치 수열(1)")
# 함수 선언
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# 함수 호출
print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))
# 위와 같이 코드 작성할 경우 처리에 시간이 오래 걸리는 문제 발생
print()

print("# 재귀 함수로 구현한 피보나치 수열(2)")
# 변수 선언
counter = 0
# 함수 선언
def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# 함수 호출
fibonacci(10)
print("ㅡㅡㅡ")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
print()

print("# 메모화")
# 메모 변수를 만듭니다.
dictionary = {
    1: 1,
    2: 2
}
# 함수 선언
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
# 함수를 호출
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

