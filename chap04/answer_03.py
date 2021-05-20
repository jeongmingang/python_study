print("# 확인문제 1")
print(list(range(5)))
print(list(range(4, 6)))
print(list(range(7, 0, -1)))
print(list(range(3, 8)))
print(list(range(3, 9 + 1, 3)))
print()

print("# 확인문제 2")
# 숫자 무작위 입력
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)
print()

print("# 확인문제 3")
# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다.
# 몇을 더할 때 1000을 넘는지 구해 보세요. 그리고 그때의 값도
# 출력해보세요. 다음은 1000이 넘는 경우를 구한 예입니다.
limit = 10000
i = 1
# sum 은 파이썬 내부에서 사용하는 식별자이므로 sum_value 라는 변수 이름을 사용함
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))
print()

print("# 확인문제 4")
# 1부터 100까지의 숫자가 있다고 합시다. 계산시 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾아주세요.
# 1 * 99, 2* 98, 3 * 97, ..., 98 * 2, 99 * 1
# 반복문을 사용
max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

# 최댓값 구하기
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
