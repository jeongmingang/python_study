list_a = ['a', 'b', 'c']

for e in list_a:
    print(e)
print()

# enumerate 인덱스 찍기
for i, v in enumerate(list_a):
    print(i, v)

a, b = 97, 40
x, y = divmod(a, b)     # 몫, 나머지
print("x =", x, "y =", y)
