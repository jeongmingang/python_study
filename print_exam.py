print("#하나만 출력")
print()

print("#하나만 출력2", "abcd", sep="\n", end="\n\n")
print("결과", end="\n\n")

print(type('하나만'), type(12), type(12.5), sep="\n", end="\n\n")

print("이름\t\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t\t3\t강서구", end="\n\n")

# print("안녕하세요" + 1)  # 문자열과 숫자 사이에는 사용불가
# print("안녕하세요" * 3)  # 문자열을 숫자와 *연산자로 연결
print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print()
print("안녕하세요"[0:4], end="\n")
print("안녕하세요"[:3], end="\n")    # 앞의 값 생략 : 0번째부터 뒤의 숫자 n번째 앞의 문자까지
print("안녕하세요"[3:], end="\n\n")    # 뒤의 값 생략 : n번째부터 끝의 문자까지

hello = "안녕하세요"
print(type(hello), hello[:2], hello, sep='\n', end="\n\n")

print(len("안녕하세요"), end="\n\n")

res = input("인사말을 입력하세요")
print("입력한 답은", res, end="\n\n")

a = "10 11 a b 14".split(" ")
print(type(a), a, sep='\n')

x, y, z = 10, 20, 30
print(x, y, z, sep='\n', end="\n\n")

print(x, y, sep='\n', end="\n")
print("x와 y의 값 스왑 가능")
x, y = y, x
print(x, y, sep='\n', end="\n")

