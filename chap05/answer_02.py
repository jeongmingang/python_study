print("# 확인문제 1")
# 재귀함수로 만들어 리스트를 평탄화하는 함수를 만들어보세요.
# 중첩된 리스트가 있을 때 중첩 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 리스트 평탄화라 합니다.
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

