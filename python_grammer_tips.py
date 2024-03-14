# 리스트 안 원소들 공백으로 구분하여 출력하기
# 1 2 3 4
# 1 2 ... 20
print(*[1, 2, 3, 4])
print(*[range(1, 21)])


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
print("4321"[::-1])  # 역순출력


# 내포 표기 생성
print(*[num for num in range(1, 11) if not num % 2])


# while 선언시 변수 할당
# a에 0 입력할때까지 계속 출력
while a := int(input()):
    print(a)


# 리스트의 특정 범위 변경
a = [1, 2, 2, 3]
a[2:4] = [3, 4]


# 배열에서 서브배열 제외하기
[1, 2, 3, 4, 5] - [1, 3, 5]
{1, 2, 3, 4 ,5} - {2, 4}


# 아스키코드 변환
ord("A")   # A의 아스키코드
chr(12)    # 12 아스키코드에 해당하는 값


# 문자열 합성
# 구분자.join(iterable)
" ".join(["apple", "banana", "grape"])


# 문자열 정렬
"*".center(10, "-")
"*".ljust(10, "-")
"*".rjust(10, "-")