import sys
sys.stdin = open('p1961.txt', 'r')

import copy

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    copy_arr = [[0] * N for _ in range(N)]
    result = ["" for _ in range(N)]
    for r in range(3):
        for i in range(N):
            for j in range(N):
                result[i] += str(arr[N-j-1][i])
                copy_arr[i][j] = arr[N-j-1][i]
            result[i] += " "
        arr =copy.deepcopy(copy_arr)

    print(f'#{t}')
    for data in result:
        print(data.rstrip())


"""
arr
1 2 3
4 5 6
7 8 9

copy -> arr
7 4 1
8 5 2
9 6 3

copy2 -> arr
9 8 7
6 5 4
3 2 1

copy3
"""