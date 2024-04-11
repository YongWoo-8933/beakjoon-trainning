# 시간 계산은 나머지 개념 활용하기
# ex) 46분 이전 x분, 이후 x분 구하기
x = 52
after_x = (46 + x) % 60
before_x = (46 - x) % 60


# 넓이 구할때 배열 활용
# ex) 100x100 넓이에서 뭔가 작업을 한다면, 
#     모든 값이 0인 100x100배열 만들어 논리 전개


# 둘중 더 큰값, 작은값 내보낼 땐 min max 사용


# 최대공약수 => 유클리드 호제법
# 최소공배수 => (a*b)//gcd(a,b)


# in list 시간복잡도 => O(n)
# in set 시간복잡도 => O(1)


# pop(0) 시간복잡도 => O(n)


# 1차원 배열을 loop로 돌리는 방법
# i=0에서 i++ 하되, 전체 배열의 크기를 n이라하면
# i=(i+1)%n 값으로 두면 i가 계속 돌아감


# str의 index화 => dict자료형 활용


# n까지의 소수를 구하는 또다른 방법
# 주로 소수의 갯수를 셀때 유리함
t = 246912
x = [0, 0]+[1]*(t-1)
for i in range(int(t**.5)+1):
    if x[i]: x[2*i::i] = [0]*(t//i - 1)


# 루프를 종료하고 답을 제출하고싶을땐
# return이 아니라 exit(0)를 사용하자..