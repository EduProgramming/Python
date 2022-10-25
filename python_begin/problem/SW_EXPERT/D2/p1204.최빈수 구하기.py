T = int(input())
for t in range(1,T+1):
    test_num = int(input())
    scores = list(map(int, input().split()))
    scores_cnt = [0 for i in range(101)]
    max_idx = 0
    res = 0

    #counting - reverse
    for i in range(len(scores)):
        scores_cnt[100-scores[i]] += 1

    #find max_index
    for i in range(101):
        max_idx = scores_cnt[i] if scores_cnt[i] > max_idx else max_idx
    
    for i in range(101):
        if scores_cnt[i] == max_idx:
            res = 100-i
            break
    print(f"#{t} {res}")