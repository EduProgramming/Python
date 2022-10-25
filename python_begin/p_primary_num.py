result = []

N = int(input())
for i in range(2, N+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        result.append(i)

print(result)

"""
소수: 해당 값이 나 자신과, 1이 약수인지를 판별...
-> 2이상의 값 -> 나 자신만 약수가 되면 됩니다.
"""

# result = []

# N = int(input())
# visited = [0] * (N+1)

# for i in range(2, N+1):
#     if visited[i] == 0:
#         result.append(i)
#         for j in range(2*i, N+1, i):
#             visited[j] = 1

# print(result)