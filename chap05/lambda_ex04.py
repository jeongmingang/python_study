print("# 이전 코드를 람다로 변경")
"""
def power(item):
    return item * item
"""
power = lambda x: x * x

"""
def under_3(item):
    return item < 3
"""

under_3 = lambda x: x < 3

list_input_a = {1, 2, 3, 4, 5}

# map 함수
output_a = map(lambda x: x * x, list_input_a)
# 값을 제곱하여 출력
print(list(output_a))

# filter 함수
output_b = filter(lambda x: x < 3, list_input_a)
# x < 3이 Ture 인 리스트를 출력
print(list(output_b))


output_c = lambda x, y: x * y
# x, y를 곱하여 출력
res = output_c(5, 3)
print(res)

