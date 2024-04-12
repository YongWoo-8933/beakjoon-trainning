"""
입력
입력 데이터는 표준 입력을 사용한다. 
입력은 T개의 테스트 데이터로 구성된다. 
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터는 한 줄로 구성된다. 각 줄에는 네 개의 정수 M, N, x와 y가 주어진다. 
(1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N) 여기서 <M:N>은 카잉 달력의 마지막 해를 나타낸다.

출력
출력은 표준 출력을 사용한다. 
각 테스트 데이터에 대해, 정수 k를 한 줄에 출력한다. 
여기서 k는 <x:y>가 k번째 해를 나타내는 것을 의미한다. 
만일 <x:y>에 의해 표현되는 해가 없다면, 
즉, <x:y>가 유효하지 않은 표현이면, -1을 출력한다.

예제 입력 1 
3
10 12 3 9
10 12 7 2
13 11 5 6
예제 출력 1 
33
-1
83
"""
from sys import stdin
import math
input()
for i in stdin:
    M, N, x, y = map(int, i.split())
    if abs(x-y) % math.gcd(M, N):
        print(-1)
    else:
        count = 0
        while x or y:
            if x<1:
                x = M
            if y<1:
                y = N
            z = min(x, y)
            x-=z
            y-=z
            count += z
        print(count)
    


