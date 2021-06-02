PI = 3.141592


def number_input():
    output = input("숫자 입력 >")
    return float(output)


# 원의 둘레
def get_circumference(radius):
    return 2 * PI * radius


# 원의 넓이
def get_circle_area(radius):
    return PI * radius * radius


# 활용 예
# 현재 파일이 엔트리 포인트일 때만 실행
if __name__ == "__main__":
    print("get_circumference(10) :", get_circumference(10))
    print("get_circle_area(10) :", get_circle_area(10))