# 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점
print("# if 조건문과 여러 줄 문자열(1)")
# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문으로 홀수 짝수를 구분
# 들여쓰기가 문자열에 포함
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다. """.format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다. """.format(number, number))
print()

print("# if 조건문과 여러 줄 문자열(2)")
# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문으로 홀수 짝수를 구분
# 실행결과는 제대로 나오지만 코드가 이상한 구조
if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다. """.format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다. """.format(number, number))
print()

# 괄호로 문자열 연결 - 괄호 내부에 문자열을 여러개 입력하면 모든 문자열을 합친 새로운 문자열이 만들어짐
print("# 괄호로 문자열 연결")
# 변수 선언
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)
print("test :", test)
# 'str' = 문자열 자료형입니다.
print("type(test) :", type(test))
print()

print("여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1) - 괄호로 문자열 연결")
# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문으로 홀수 짝수를 구분
if number % 2 == 0:
    print((
        # 줄바꿈을 하기 위해서는 마지막을 제외(<--반드시 주의)한 문자열 뒤에 \n을 입력
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다. "
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다. "
    ).format(number, number))
print()

# 문자열의 join() 함수
print("여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(2) - join() 함수 이용")
# 변수 선언
number = int(input("정수 입력 > "))

# if 조건문으로 홀수 짝수를 구분
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다. "
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다. "
    ]).format(number, number))
print()
