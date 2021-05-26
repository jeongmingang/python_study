# 함수 내부에 yield 키워드 사용하면 해당 함수는 제너레이터 함수 됨
# 일반 함수와 달리 호출해도 함수 내부 코드가 실행되지 않음
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
