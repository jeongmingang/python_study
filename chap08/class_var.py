class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        # 클래스 내,외부에서 클래스 변수에 접근시 Student.count 형태(클래스 이름.변수 이름)를 사용함
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))


# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("운명월", 64, 88, 92, 92)
]

# 출력
print()
# 클래스 내,외부에서 클래스 변수에 접근시 Student.count 형태(클래스 이름.변수 이름)를 사용함
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))

