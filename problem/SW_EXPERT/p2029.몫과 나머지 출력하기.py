T = int(input())
for t in range(1, T+1):
    M, N = map(int, input().split())
    print("#{} {} {}".format(t, M//N, M%N))

# #방도2
# res = []
# T = int(input())
# for t in range(1, T+1):
#     M, N = map(int, input().split())
#     res.append("#{} {} {}".format(t, M//N, M%N))
# for i in range(len(res)):
#     print(res[i])