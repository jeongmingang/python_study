print("# 확인문제 1")
numbers = [1, 2, 3, 4, 5, 6]

print("::".join(map(str, numbers)))
print()

print("# 확인문제 2")
numbers = list(range(1, 10 + 1))

print("원본 :", numbers, end='\n\n')

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("# 제곱하여 50미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))

