# 딕셔너리 선언
print("# 딕셔너리의 요소에 접근하기")
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])
print()

# 리스트 안의 특정 값 출력하려는 경우
print("# 리스트 안의 특정 값 출력하려는 경우")
print("ingredient [1]:", dictionary["ingredient"][1])
print()

# 딕셔너리 선언
dictionary = {}

# 요소 추가 전에 내용을 출력
print("# 요소 추가 전에 내용을 출력")
print("요소 추가 이전:", dictionary)

# 딕셔너리에 요소를 추가
dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

# 출력
print("요소 추가 이후:", dictionary)
print()

# 요소 제거 전에 내용을 출력
print("# 요소 제거 전에 내용을 출력")
print("요소 제거 이전:", dictionary)

# 딕셔너리의 요소를 제거
del dictionary["name"]
del dictionary["head"]
del dictionary["body"]

# 출력
print("요소 제거 이후:", dictionary)


