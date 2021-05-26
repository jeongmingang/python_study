# open(), closed() 함수
# 파일을 엽니다.
file = open("basic.txt", "w")
# 파일에 텍스트를 씁니다. (변경시 덮어씀)
file.write("Hello Python Programming...")
# 파일을 닫습니다.
file.close()

# with 키워드
# 파일을 엽니다.
with open("basic.txt", "w") as file:
    # 파일에 텍스트를 씁니다. (변경시 덮어씀)
    file.write("Hello Python Programming...!")

# read() 함수
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)
