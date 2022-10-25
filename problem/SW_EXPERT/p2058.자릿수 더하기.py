N = int(input())
M = list(map(int, input().split()))
M.sort()

print(M[N//2])