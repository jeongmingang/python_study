import os.path

std_list = []
with open("std_list.txt", "r", encoding="utf-8") as f:
    for line in f:
        std = line.strip().split(",")
        print("std :", std)
        std = int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4])
        std_list.append(list(std))


std_list = [
    [1, "김승영", 90, 90, 90],
    [2, "지재삼", 80, 90, 80]]
if not os.path.exists("std_list.txt"):
    with open("std_list.txt", "w", encoding="UTF-8") as f:
        for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
            f.write(format_str)


print("{:3} {:4} {:3} {:3} {:3} {:4} {:>4}".format('번호', '성명', '국어', '영어', '수학', '총점', '평균'))
for std in std_list:
    total = std[2] + std[3] + std[4]
    avg = total/3
    std_info = "{:3d} {:5} {:3d} {:3d}  {:3d} {:4d} {:7.2f}".format(int(std[0]), std[1], int(std[2]), int(std[3]),
                                                                    int(std[4]), total, avg)
    print(std_info)


std_info = [[3, "테스트", 90, 90, 90]]
with open("std_list.txt", "a", encoding="UTF-8") as f:
    for std in std_info:
        format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
        f.write(format_str)
        std_info = "{:3d} {:5} {:3d} {:3d}  {:3d} {:4d} {:7.2f}".format(int(std[0]), std[1], int(std[2]), int(std[3]),
                                                                        int(std[4]), total, avg)
        print(std_info)



