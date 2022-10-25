N = int(input())
nums = []
for i in range(1,N+1):
    if N%i == 0:
        nums.append(i)

print(" ".join(map(str,nums)))



# #방법2
# N = int(input())
# nums = ""
# for i in range(1,N+1):
#     if N%i == 0 and i == N:
#         nums += str(i)
#     elif N%i == 0:
#         nums += str(i) + " "

# print(nums)