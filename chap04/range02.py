# for 반복문과 범위를 함께 조합하여 사용
print("# for 반복문과 범위를 함께 조합하여 사용")
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")
print()

# 리스트와 범위를 조합하여 사용
print("# 리스트와 범위를 조합하여 사용")
# 리스트 선언
array = [273, 32, 103, 57, 52]

# 리스트에 반복문 적용
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))
print()

# for 반복문 : 반대로 반복하기
print("# 역반복문")
# 역반복문
for i in range(4, 0 -1, -1):
    print("현재 반복 변수 : {}".format(i))
print()


