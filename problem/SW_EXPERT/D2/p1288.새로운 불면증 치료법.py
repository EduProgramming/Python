res=[]
for t in range(1, int(input())+1):
    nums = set()
    N = int(input())
    M = N
    cnt = 0
    while True:
        str_N = str(M)
        cnt += 1
        for i in range(len(str_N)):
            nums.add(int(str_N[i]))
        if len(nums) == 10:
            res.append("#"+str(t)+" "+str(str_N))
            break
        M = N*(cnt+1)
for i in range(len(res)):
    print(res[i])