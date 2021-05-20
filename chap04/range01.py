print("숫자를 한 개 넣은 범위")
a = range(5)
print(a)
print(list(range(10)))

print("숫자를 두 개 넣은 범위")
print(list(range(0, 5)))
print(list(range(5, 10)))

print("숫자를 세 개 넣은 범위")
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))

print("매개변수 내부에 수식을 사용")
a = range(0, 10 + 1)
print(list(a))

print("실수를 정수로 바꾸는 방법")
n = 10
a = range(0, int(n / 2))
print(list(a))

print("정수 나누기 연산자 사용")
a = range(0, n // 2)
print(list(a))