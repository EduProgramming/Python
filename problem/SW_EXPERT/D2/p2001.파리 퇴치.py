T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for y in range(M):
                for x in range(M):
                    cnt += arr[i+y][j+x]
            if cnt > result:
                result = cnt

    print(f'#{t} {result}')