print("# 확인문제 1")
dict_a = {
    "name": "구름",
}
print(dict_a)

del dict_a["name"]
print(dict_a)
print()

print("# 확인 문제 2")
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

# 숫자와 문자열 사이에 빈칸이 없게 출력
print("# 우리 동네 애완 동물들")
for pet in pets:
    print(pet["name"], str(pet["age"]) + "살")
print()

print("# 확인 문제 3")
# 숫자 무작위 입력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 6, 7, 3, 5, 7, 8, 3, 5, 3, 5, 9, 7, 4, 4, 2, 6, 8]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1

# 출력
# numbers 내부에 있는 숫자가 몇 번 등장하는지를 출력
print(counter)
print()

print("# 확인 문제 4")
# 딕셔너리 선언
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀 플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반목문을 사용
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])

