import sys
sys.stdin = open('p1288.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    set_data = set()
    cnt = 1
    while len(set_data) != 10:
        for num in str(N * cnt):
            set_data.add(num)
        cnt += 1
    print(f'#{t} {N * (cnt-1)}')