# next() 함수 사용해 내부 코드 실행
# yield 키워드 부분까지만 실행하며 next() 함수 리턴값으로 yield 키워드 뒤에 입력한 값이 출력됨

def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

# 함수 호출
output = test()

# next() 함수 호출
print("D 지점 통과")
a = next(output)
print(a)

print("E 지점 통과")
b = next(output)
print(b)

print("F 지점 통과")
c = next(output)
print(c)

# 한번 더 실행
# next() 함수 호출한 이후 yield 키워드 만나지 못하고 함수 끝나면 StopIteration 예외 발생
next(output)
