
list_a = [273, 32, 103, "문자열", True, False]
list_b = [i for i in list_a]
print(type(list_b),list_b)

# 0~100까지 짝수만 list(even_list)에 저장 후 출력
print("# 0~100까지 짝수만 list(even_list)에 저장 후 출력")
even_list = [i for i in range(101) if i % 2 == 0]
print(even_list)
print()

# 0~100까지 홀수만 list(odd_list)에 저장 후 출력
print("# 0~100까지 홀수만 list(even_list)에 저장 후 출력")
odd_list = [i for i in range(101) if i % 2 == 1]
print(odd_list)
print()

# 확인 문제
print("확인문제 2")
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numberTo100 = [i for i in numbers if i >= 100]
print("100 이상의 수", numberTo100)
print()

print("확인문제 4")
list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for sub_list in list_of_list:
    for i in sub_list:
        print(i)
print()

print("확인문제 5")
list_seq = [i for sub_list in list_of_list for i in sub_list]
print("list_seq ", list_seq)
print()



