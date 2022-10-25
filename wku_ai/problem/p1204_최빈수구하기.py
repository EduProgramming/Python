import sys
sys.stdin = open('./p1204.txt', 'r')

T = int(input())
for a in range(1, T+1):
    t = int(input())
    scores = list(map(int ,input().split()))
    count_list = [0] * 101 #0~100
    for score in scores:
        count_list[score] += 1
    
    max_cnt = max(count_list)
    idx = 0
    for i in range(len(count_list)-1, -1, -1):
        if count_list[i] == max_cnt:
            idx = i
            break

    print(f'#{t} {idx}')
    