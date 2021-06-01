import sys

# 명령 매개 변수를 출력
print(sys.argv)
print("ㅡㅡㅡ")

# 컴퓨터 환경과 관련된 정보를 출력
print("get windows version :()", sys.getwindowsversion())
print("ㅡㅡㅡ")
print("copyright :", sys.copyright)
print("ㅡㅡㅡ")
print("version :", sys.version)

# 프로그램을 강제로 종료
sys.exit()