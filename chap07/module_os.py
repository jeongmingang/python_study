import os

# 기본 정보 몇개 출력
print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더 내부의 요소 :", os.listdir())

# 폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
print("폴더를 만듬", os.mkdir("hello"))
print("폴더를 제거", os.rmdir("hello"))

# 파일을 생성하고 파일 이름을 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일 제거
os.remove("new.txt")

# 시스템 명령어 실행
os.system("dir")