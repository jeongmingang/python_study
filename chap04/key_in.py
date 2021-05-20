# in 키워드
print("# 딕셔너리 내부에 키가 있는지 확인하기 - in 키워드")

# 딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 입력받기
key = input("> 접근하고자 하는 키: ")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()

# get() 함수
print("# 키가 존재하지 않을때 None을 출력 - get() 함수")

# 존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()

# for 반복문 : 딕셔너리와 함께 사용
print("# for 반복문 : 딕셔너리와 함께 사용")

# for 반복문을 사용
for key in dictionary:
    # 출력
    print(key, ":", dictionary[key])


