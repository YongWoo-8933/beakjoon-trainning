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
# 아래처럼 할당과 비교를 동시에 할수도 있음
while (s:=input()) != "0":
    print(s)


# 리스트의 특정 범위 변경
a = [1, 2, 2, 3]
a[2:4] = [3, 4]


# set에서 차집합 구하기
{1, 2, 3, 4 ,5} - {2, 4}


# 두 리스트 동시 연산 => zip 활용
a = [1, 2, 3]
b = [4, 5, 6]
print([ai - bi for ai, bi in zip(a, b)])


# 아스키코드 변환
ord("A")   # A의 아스키코드
chr(12)    # 12 아스키코드에 해당하는 값


# 문자열 합성
# 구분자.join(iterable)
" ".join(["apple", "banana", "grape"])


# 문자열 대소문자 내장함수
"aBcDeFg".isuuper()     # False
"aBcDeFg".islower()     # False
"aBcDeFg".upper()       # ABCDEFG
"aBcDeFg".lower()       # abcdefg
"aBcDeFg".swapcase()    # AbCdEfG


# 문자열 정렬
"*".center(10, "-")
"*".ljust(10, "-")
"*".rjust(10, "-")


# 문자열 내 숫자 표기시 0 채우기
str(5).zfill(2)   # "05"


# 파이썬 정규 표현식 사용
import re
print(re.search('a', 'bba'))
# <re.Match object; span=(2, 3), match='a'>
print(re.findall('\d', '숫자123이 이렇게56 있다8'))
print(re.findall('\d+', '숫자123이 이렇게56 있다8'))
# ['1', '2', '3', '5', '6', '8']
# ['123', '56', '8']
print(re.fullmatch('a', 'a'))
print(re.fullmatch('a', 'aaa'))
print(re.fullmatch('a', 'baa'))
# <re.Match object; span=(0, 1), match='a'>
# None
# None


# 람다 함수
func = lambda x,y: x + y
print(func(1, 2))


# sorted함수의 key 사용
my_list = ["api", "app", "carrier", "demon", "aaa"]
sorted(my_list, key= lambda x : (len(x), x))
sorted("adbbarki", "adbbarki".find)    # aadbbrki


# 파이썬 진수변환
int("Z34AB", 36)


# 내장 산술 연산
Q, R = divmod(36, 10)   # Q: 3, R: 6
int(5.3+0.5)   # 5.3 반올림 => round 사용금지!!!!
pow(5, 3)    # 5^3


# 콤비네이션(경우의수)
import math
math.comb(5,2)


# 조합 직접 주하기
import itertools
itertools.combinations([1, 2, 3], 2)    # [(1, 2), (2, 3), (1, 3)]


# 문자열 / 숫자 판별
"123".isdigit()       # True
"33ffold".isdigit()   # False
"ffold".isalpha()   # True
"33ffold".isalpha()   # False


# 최대 공약수, 최소 공배수
import math
math.gcd(8,14)    # 2
math.lcm(10,16)   # 80


# 원 리스트형 문제
import collections
collections.deque([1,2,3,4,5]).rotate(1)   # [5,1,2,3,4]
collections.deque([1,2,3,4,5]).rotate(-1)   # [2,3,4,5,1]