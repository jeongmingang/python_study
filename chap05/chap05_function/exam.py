# 구구단 세로로 출력 (시험)
print("# 구구단 세로로 출력")


def dan(num):
    print("{}".format(num) + "단")
    for i in range(1, 10):
        print('{} * {} = {:2}'.format(num, i, num * i))


def gugudan():
    for i in range(2, 10):
        dan(i)


if __name__ == "__main__":
    gugudan()
print()


# 구구단 가로로 출력 해보세요 (시험)
print("# 구구단 가로로 출력")


def gugudan2():
    for second in range(1, 10):
        for first in range(2, 10):
            print('{} * {} = {}'.format(first, second, first * second), end='\t')
        print()


if __name__ == "__main__":
    gugudan2()
print()


# 시험 두번째 문제
print("# 시험 두번째 문제")


def solution1(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])
    return answer

# 축약 버전
# 1. i= x[0], j = x[1], k = x[2]
# 2. x[0], x[1]로 slice
# 3. 그 결과를 sorted()를 이용해 정렬
# 4. x[2]를 이용해 정렬
# 5. list 를 이용해 출력

def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]  # 2차원 리스트

result1 = solution1(array, commands)
print(type(result1), result1)  # list [5, 6, 3]

result2 = solution2(array, commands)
print(type(result2), result2)  # list [5, 6, 3]
print()


# 시험 두번째 문제 답
def solution3(array, commands):
    answer = []
    for a, b, c in commands:
       answer += [sorted(array[a-1:b])[c-1]]
    return answer

def solution4(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]


if __name__ == "__main__":
    res = solution3([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(type(res), res)

    res = solution4([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(type(res), res)

print()

# 문제
print("# 딕셔너리 활용")

list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
# 변수 = {키: 값{키: 값, 키: 값}, 키: 값{키: 값, 키: 값, 키: 값}, 키: 값{키: 값}
dict_a = {'k': {'a': 10, 'b': 20}, 'l': {'a': 10, 'b': 20, 'c': 40}, 'm': {'a': 10}}

for key in dict_a:
    print(key, "=>", dict_a[key])


print()

print(list_a[0][0], list_a[0][1])
print(list_a[1][0], list_a[1][1], list_a[1][2], list_a[1][3])
print(list_a[2][0], list_a[2][1])
print(list_a[3][0], list_a[3][1], list_a[3][2])



