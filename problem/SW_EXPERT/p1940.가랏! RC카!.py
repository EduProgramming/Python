res = []
T = int(input())
for t in range(T):
    s = 0
    v = 0
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if arr[i][0] == 1:
            v += arr[i][1]
        elif arr[i][0] == 2:
            if v == 0 :
                v = 0
            else:
                v -= arr[i][1]
        s += v
    res.append(s)
    print(f"#{t+1} {res[t]}")
