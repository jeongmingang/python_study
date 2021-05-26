def power(item):
    return item * item


def under_3(item):
    return item < 3


list_input_a = {1, 2, 3, 4, 5}

# map 함수
output_a = map(power, list_input_a)
# 값을 제곱하여 출력
print(list(output_a))

# filter 함수
output_b = filter(under_3, list_input_a)
# item < 3이 Ture 인 리스트를 출력
print(list(output_b))


