from urllib import request

# urlopen() 함수 : URL 주소의 페이지 열기

print("# urlopen() 함수로 구글의 메인 페이지를 읽습니다.")
target = request.urlopen("https://google.com")
output = target.read()

print(output)