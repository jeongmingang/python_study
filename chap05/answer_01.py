print("# 확인문제 1")
print("f(x)=x")
def f(x):
    return x
print(f(10))
print("f(x)=2x+1")
def f(x):
    return x * 2 + 1
print(f(10))
print("f(x)=x*x+2x+1")
def f(x):
    return x ** 2 + x * 2 + 1
print(f(10))
print()

print("# 확인문제 2")
# 매개변수로 전달된 값들을 모두 곱하여 리턴하는 가변 매개변수 함수
def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output  # 리턴
# 함수 호출
print(mul(5, 7, 9, 10))
print()

print("# 확인문제 3")
# 오류 발생
# def function(*values, valueA, valueB):
#     pass
# function(1, 2, 3, 4, 5)
# print()

def function(*values, valueA=10, valueB=20):
    pass
function(1, 2, 3, 4, 5)
print()

def function(valueA, valueB, *values):
    pass
function(1, 2, 3, 4, 5)
print()

def function(valueA=10, valueB=20, *values):
    pass
function(1, 2, 3, 4, 5)
