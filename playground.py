"""
문제
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
x는 231보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.

출력
입력에서 0이 주어진 횟수만큼 답을 출력한다. 
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

예제 입력 1 
9
0
12345678
1
2
0
0
0
0
32
예제 출력 1 
0
1
2
12345678
0


1
10
2
30
40
300
400
25
0
0
"""
from sys import stdin
from collections import deque
stdin.readline()
heap = deque()
for i in stdin:
    option = int(i)
    if option:
        heap.append(option)
        child = len(heap)-1
        parent = (child-1)//2
        while child and heap[child] < heap[parent]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = (child-1)//2
    else:
        if len(heap)>1:
            print(heap.popleft())
            heap.appendleft(heap.pop())
            parent = 0
            last_idx = len(heap)-1
            while parent < last_idx:
                l_child = parent*2+1
                r_child = parent*2+2
                if r_child <= last_idx:
                    if heap[l_child] <= heap[r_child] and heap[l_child] < heap[parent]:
                        heap[parent], heap[l_child] = heap[l_child], heap[parent]
                        parent = l_child
                    elif heap[r_child] < heap[l_child] and heap[r_child] < heap[parent]:
                        heap[parent], heap[r_child] = heap[r_child], heap[parent]
                        parent = r_child
                    else:
                        break
                elif l_child <= last_idx and heap[l_child] < heap[parent]:
                    heap[parent], heap[l_child] = heap[l_child], heap[parent]
                    parent = l_child
                else:
                    break
        elif len(heap)==1:
            print(heap.pop())
        else:
            print(0)
















