print("elif 구문 ㅡㅡㅡ 계절 구하기")

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고 쉽게 사용할 수 있게 월을 변수에 저장
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절 확인
if 3 <= month <= 5:
    print("현재는 봄입니다.", end="\n\n")
elif 6 <= month <= 8:
    print("현재는 여름입니다.", end="\n\n")
elif 9 <= month <= 11:
    print("현재는 가을입니다.", end="\n\n")
else:
    print("현재는 겨울입니다.", end="\n\n")

print("유머를 조건문으로 구현하기 - 1")
# 변수 선언
score = float(input("학점 입력 > "))

# 조건문 적용
# 위에서 제외된 조건을 한 번 더 검사하여 비효율적
if score == 4.5:
    print("신", end="\n\n")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑", end="\n\n")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자", end="\n\n")
elif 2.8 <= score < 3.5:
    print("일반인", end="\n\n")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민", end="\n\n")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자", end="\n\n")
elif 1.0 <= score < 1.75:
    print("불가축천민", end="\n\n")
elif 0.5 <= score < 1.0:
    print("자벌레", end="\n\n")
elif 0 <= score < 0.5:
    print("플랑크톤", end="\n\n")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗", end="\n\n")

print("유머를 조건문으로 구현하기 - 2")
# 변수 선언
score = float(input("학점 입력 > "))

# 조건문 적용
# 하위 값만 검사하고 상위 값은 검사를 생략, 조건 비교를 반으로 줄이고 코드 가독성 향상됨
if score == 4.5:
    print("신", end="\n\n")
elif 4.2 <= score:
    print("교수님의 사랑", end="\n\n")
elif 3.5 <= score:
    print("현 체제의 수호자", end="\n\n")
elif 2.8 <= score:
    print("일반인", end="\n\n")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민", end="\n\n")
elif 1.75 <= score:
    print("오락문화의 선구자", end="\n\n")
elif 1.0 <= score:
    print("불가축천민", end="\n\n")
elif 0.5 <= score:
    print("자벌레", end="\n\n")
elif 0 < score:
    print("플랑크톤", end="\n\n")
else:
    print("시대를 앞서가는 혁명의 씨앗", end="\n\n")