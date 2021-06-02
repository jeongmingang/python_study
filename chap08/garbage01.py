# 가비지 컬렉터 (garbage collector)
# • 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할

# • 예시 – 변수에 저장하지 않은 경우
print("# • 예시 – 변수에 저장하지 않은 경우")


class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))


Test("A")
Test("B")
Test("C")
print()


# • 예시 – 변수에 저장한 경우
print("# • 예시 – 변수에 저장한 경우")


class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))


a = Test("A")
b = Test("B")
c = Test("C")