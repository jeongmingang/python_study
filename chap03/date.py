# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력
# 날짜/시간 출력하기
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초", end="\n\n")

print("ㅡㅡㅡㅡ날짜/시간을 한 줄로 출력하기")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
), end="\n\n")

print("ㅡㅡㅡㅡ오전과 오후를 구분하는 프로그램")
# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour), end="\n\n")

print("ㅡㅡㅡㅡ계절을 구분하는 프로그램")
# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month), end="\n\n")

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month), end="\n\n")

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month), end="\n\n")

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month), end="\n\n")

print("ㅡㅡㅡㅡ끝자리로 짝수와 홀수 구분")
# 입력
number = input("정수 입력 > ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다", end="\n\n")

# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다", end="\n\n")

print("ㅡㅡㅡㅡin 연산자를 활용한 수정")
# 입력
number = input("정수 입력 > ")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":
    print("짝수입니다", end="\n\n")

# 짝수 조건
if last_character in "13579":
    print("홀수입니다", end="\n\n")

print("ㅡㅡㅡㅡ나머지 연산자를 활용한 짝수와 홀수 구분")
# 입력
number = input("정수 입력 > ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다")

# 홀수 조건
if number % 2 == 1:
    print("홀수입니다")