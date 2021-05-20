# while 반복문: break 키워드/continue 키워드

# 변수 선언
numbers = [5, 15, 6, 20, 7, 25]

# 반복
for number in numbers:
    # number 가 10 보다 작으면 다음 반복으로 넘어감
    if number < 10:
        continue
print(number)

