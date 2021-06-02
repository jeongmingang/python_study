# "from test_package import *"로 모듈을 읽어 들일때 가져올 모듈

# 사용시 읽어들일 모듈의 목록
__all__ = ["module_a", "module_b"]

# 패키지를 읽어 들일 때 처리를 작성
print("test_package 를 읽어 들였습니다.")