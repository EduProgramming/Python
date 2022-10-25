import sys
sys.stdin = open('./p1959.txt', 'r')

"""
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
"""

def f(min_list, max_list):
    max_cnt = 0
    for i in range(len(max_list) - len(min_list) + 1):
        cnt = 0
        for j in range(len(min_list)):
            cnt += max_list[i+j] * min_list[j]
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int ,input().split()))
    B = list(map(int ,input().split()))
    max_cnt = 0
    if N > M: #A길이가 더 길 때
        max_cnt = f(B, A)
    else: #B길이가 더 길거나 같을 때
        max_cnt = f(A, B)

    print(f'#{t} {max_cnt}')

