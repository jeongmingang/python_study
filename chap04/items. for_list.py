# 딕셔너리와 items() 함수를 함께 사용시 키와 값을 조합하여 쉽게 반복문 작성이 가능
# 변수 선언
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

# 딕셔너리의 items() 함수 결과 출력
print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

# for 반복문과 items() 함수 조합하여 사용
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print()

# 리스트 내포 - 반복문을 사용하여 리스트 재조합
print("# 리스트 내포")
# 변수 선언
array = []

# 반복문 적용
for i in range(0, 20, 2):
    array.append(i * i)
print(array)
print()

# 리스트 안에 for 문 사용
print("# 리스트 안에 for 문 사용")

# 리스트 선언
# range(0, 20, 2)의 요소를 i라고 할때 i*i로 리스트를 재조합하는 코드
array = [i * i for i in range(0, 20, 2)]
print(array)
print()

# 조건을 활용한 리스트 내포
print("# 조건을 활용한 리스트 내포")
# 리스트를 선언
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)
print()

