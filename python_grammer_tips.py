# 리스트 안 원소들 공백으로 구분하여 출력하기
# 1 2 3 4
print(*[1, 2, 3, 4])


# 배열 안 최대/최소값
max([1, 2, 3, 4])
min([1, 2, 3, 4])


# 배열 원소 모두합
sum([1, 2, 3, 4])


# string 연속출력
print("nice!! " * 10)


# 공백으로 구분되어 입력된 원소 형변환해서 받기
x, y = map(int, input("x, y에 입력할 값 공백으로 구분입력(ex 7 -8): ").split())


# 여러 줄로 입력되는 값에 대해 모든 줄을 '빠르게' 받기(^Z로 종료)
import sys
for line in sys.stdin: 
    print(line)


# 파이썬 슬라이싱 [start : end : step]
print("11223344"[::2])


# 내포 표기 생성
print(*[num for num in range(1, 11) if not num % 2])


# while 선언시 변수 할당
# a에 0 입력할때까지 계속 출력
while a := int(input()):
    print(a)