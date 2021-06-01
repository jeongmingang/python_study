import os

# 기본 정보 몇개 출력
print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더 내부의 요소 :", os.listdir())

# 폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
if not os.path.exists("hello"):
    os.mkdir("hello")
    print("폴더를 만듬", os.path.exists("hello"))

if os.path.exists("hello"):
    os.rmdir("hello")
    print("폴더를 제거", not os.path.exists("hello"))

# 파일을 생성하고 파일 이름을 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일 제거
os.remove("new.txt")
# os.unlink("new.txt")

# 시스템 명령어 실행
# os.system("dir")

# std_list test (파이썬 시험)
std_list = [
    [1, "김상건", 90, 80, 70],
    [2, "이나연", 80, 60, 70],]

if not os.path.exists("std_list,txt"):
    # if os.path.isfile("std_list.txt"):
    with open("std_list.txt", "w", encoding="UTF-8") as f:
        for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
            f.write(format_str)

std_list2 = []

with open("std_list.txt", "r", encoding="utf-8") as f:
    for line in f:
        std = line.strip().split(",")
        print("std :", std, type(std))
        std = int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4])
        std_list2.append(list(std))

print("파일로 읽어 들인 std_list2[] :", std_list2)

