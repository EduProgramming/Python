import sys
sys.stdin = open('p2001.txt', 'r')

"""
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
"""


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_cnt = 0
            for x in range(M):
                for y in range(M):
                    sum_cnt += arr[x+i][y+j]
            if sum_cnt > result:
                result = sum_cnt

    print(f'#{t} {result}')